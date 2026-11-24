"""Behaviour of the timer function, with the network and Telegram replaced by fakes."""

import asyncio
from datetime import datetime, time
from types import ModuleType

import pytest

PAGE = '<html><body><p class="m">Buenos dias</p><p class="other">x</p></body></html>'


class FakeResponse:
    text = PAGE


class FakeBot:
    def __init__(self) -> None:
        self.sent: list[tuple[str, str]] = []

    async def send_message(self, chat_id: str, text: str) -> None:
        self.sent.append((chat_id, text))


async def no_sleep(_seconds: float) -> None:
    return None


@pytest.fixture
def offline(send_messages: ModuleType, monkeypatch: pytest.MonkeyPatch) -> list[str]:
    urls: list[str] = []

    def fake_get(url: str) -> FakeResponse:
        urls.append(url)
        return FakeResponse()

    monkeypatch.setattr(send_messages.requests, "get", fake_get)
    monkeypatch.setattr(send_messages.asyncio, "sleep", no_sleep)
    return urls


def test_send_morning_messages_sends_to_every_chat(
    send_messages: ModuleType, offline: list[str]
) -> None:
    bot = FakeBot()

    asyncio.run(send_messages.send_morning_messages(["1", "2"], bot))

    assert bot.sent == [("1", "Buenos dias"), ("2", "Buenos dias")]
    assert offline == [
        "https://www.wishesmsg.com/good-morning-messages-for-girlfriend/"
    ]


def test_send_night_messages_sends_to_every_chat(
    send_messages: ModuleType, offline: list[str]
) -> None:
    bot = FakeBot()

    asyncio.run(send_messages.send_night_messages(["1"], bot))

    assert bot.sent == [("1", "Buenos dias")]
    assert offline == ["https://www.wishesmsg.com/good-night-messages-for-girlfriend/"]


def test_main_sends_nothing_outside_the_windows(
    send_messages: ModuleType, offline: list[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    class Afternoon(datetime):
        @classmethod
        def now(cls, tz=None):  # type: ignore[no-untyped-def]
            return datetime.combine(datetime(2026, 1, 1), time(15, 0))

    monkeypatch.setattr(send_messages, "datetime", Afternoon)
    bot = FakeBot()
    monkeypatch.setattr(send_messages, "bot_token", bot)

    asyncio.run(send_messages.main(None))

    assert bot.sent == []
    assert offline == []
