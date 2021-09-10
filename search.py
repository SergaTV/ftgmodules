import re
from telethon import events
import requests
from uniborg.util import admin_cmd
import asyncio

bot_username = "ftg2bot"#insert bot username here
@borg.on(events.NewMessage(outgoing = True, pattern='\.search.*'))
async def _(event):
    mess = event.message.message
    m = re.search(r'\.search (.*.+)',event.message.message)
    reg_mess = m.group(1)
    await borg.send_message(bot_username, "."+reg_mess)