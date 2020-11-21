import os
import requests
from dotenv import load_dotenv

load_dotenv()

from telethon import TelegramClient, events

BOT_TOKEN = os.getenv('BOT_TOKEN')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    """Send a message when the command /start is issued."""
    await event.respond('Привет! Этот бот проверяет состояние сервера ya.ru. Введите любое сообщение чтобы узнать состояние')
    raise events.StopPropagation

@bot.on(events.NewMessage)
async def echo(event):
    """Echo the user message."""
    try:
        response = requests.get('http://ya.ru/')
    except:
        statuse = 'ошибка'
        exit
    else:
        if response.status_code == 200:
            statuse = 'всё хорошо'
        else:
            statuse = 'все сломалось'

    await event.respond(f'Запрос к серверу.... {statuse}. Тестирование завершено')
    raise events.StopPropagation

def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()