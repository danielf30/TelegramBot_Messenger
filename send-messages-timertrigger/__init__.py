import requests
import telegram
from bs4 import BeautifulSoup
from datetime import datetime, time
import asyncio
import random
import os
import azure.functions as func

num_messages_morning = 1
num_messages_night = 1

secret_value = os.environ.get('token_bot')
bot_token = telegram.Bot(token=secret_value)
secrets = {'chatbot_id1': os.environ.get('chatbot_id1'), 'chatbot_id2': os.environ.get('chatbot_id2')}
secret_value1, secret_value2 = secrets.values()
chat_ids = [secret_value1,secret_value2]

async def send_morning_messages(chat_ids, bot):
    url = 'https://www.wishesmsg.com/good-morning-messages-for-girlfriend/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    messages = soup.select('p.m')
    for i in range(num_messages_morning):
        message = random.choice(messages).text
        for chat in chat_ids:
            await bot.send_message(chat_id=chat, text=message)
            await asyncio.sleep(random.randint(1, 5))

async def send_night_messages(chat_ids, bot):
    url = 'https://www.wishesmsg.com/good-night-messages-for-girlfriend/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    messages = soup.select('p.m')
    for i in range(num_messages_night):
        message = random.choice(messages).text
        for chat in chat_ids:
            await bot.send_message(chat_id=chat, text=message)
            await asyncio.sleep(random.randint(1, 5))

async def main(mytimer: func.TimerRequest) -> None:
    current_time = datetime.now().time()
    if current_time > time(11, 58, 0) and current_time < time(12, 2, 0):
        asyncio.gather(asyncio.create_task(send_morning_messages(chat_ids, bot_token)))
    elif current_time > time(0, 58, 0) and current_time < time(1, 2, 0):
        asyncio.gather(asyncio.create_task(send_night_messages(chat_ids, bot_token)))