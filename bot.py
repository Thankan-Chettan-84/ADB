from aiohttp import web
from __init__ import web_server

import asyncio
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from pyrogram import types


API_ID = "1534768"
API_HASH = "894f663e1e289f898208e3a26f798214" 
BOT_TOKEN = "5400680150:AAHi_7wOeFhmUHDLc6jP3CynlSSg5hokUaE"

TIME = "900" 
GROUPS = "-1001886617690"
ADMINS = "1276065476"
PORT = 8080

START_MSG = "<b>You Are Not Authorised To Use This Bot</b>"


class Bot(Client):

    def __init__(self):
        super().__init__(
            name="autodelete",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=300,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

        
        
@Client.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@Client.on_message(filters.chat(GROUPS) & filters.media)
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)

        
        
app = Bot()
app.run()
print("Bot Started!")

idle()

Bot.stop()
print("Bot Stopped!")
PORT = 8080
