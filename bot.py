from aiohttp import web
from __init__ import web_server

import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = "1534768"
API_HASH = "894f663e1e289f898208e3a26f798214" 
BOT_TOKEN = "5400680150:AAHi_7wOeFhmUHDLc6jP3CynlSSg5hokUaE"

TIME = "600" 
GROUPS = "-1005932375960"
ADMINS = "1276065476"


START_MSG = "<b>Hai {},\nI'm a private bot of @mh_world to delete group messages after a specific time</b>"


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

class Bot(Client):
app = web.AppRunner(await web_server())
      await app.setup()
      bind_address = "0.0.0.0"
      await web.TCPSite(app, bind_address, PORT).start()
