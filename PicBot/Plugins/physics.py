from pyrogram import Client, filters
import re
from bs4 import BeautifulSoup
import requests

@Client.on_message(filters.command(["physics"]))
async def physics(bot, update):
     source = requests.get('https://teletype.in/@satyendra/Physics').text
     soup = BeautifulSoup(source, 'lxml')
     text = soup.article.text
     await bot.send_message(update.chat.id, text, reply_to_message_id=update.message_id)