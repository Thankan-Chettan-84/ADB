from aiohttp import web
from __init__ import web_server

import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = "1534768"
API_HASH = "894f663e1e289f898208e3a26f798214" 
BOT_TOKEN = "5400680150:AAHi_7wOeFhmUHDLc6jP3CynlSSg5hokUaE"

TIME = "900" 
GROUPS = "-1001886617690"
ADMINS = "1276065476"


START_MSG = "<b>You Are Not Authorised To Use This Bot</b>"


Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@Bot.on_message(filters.chat(GROUPS) & filters.media)
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
       
Bot.start()
print("Bot Started!")

idle()

Bot.stop()
print("Bot Stopped!")
PORT = 8080
