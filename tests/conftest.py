"""Loads the timer function by path, since its folder name is not importable."""

import importlib.util
import os
import sys
from pathlib import Path
from types import ModuleType

import pytest

FUNCTION_INIT = (
    Path(__file__).resolve().parents[1] / "send-messages-timertrigger" / "__init__.py"
)


@pytest.fixture
def send_messages() -> ModuleType:
    # The module builds a telegram.Bot at import time, which refuses an empty token.
    os.environ.setdefault("token_bot", "123456:TEST-TOKEN")
    os.environ.setdefault("chatbot_id2", "42")
    spec = importlib.util.spec_from_file_location("send_messages", FUNCTION_INIT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["send_messages"] = module
    spec.loader.exec_module(module)
    return module
