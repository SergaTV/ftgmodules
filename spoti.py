
from telethon import events
import requests
from uniborg.util import admin_cmd
import asyncio

bot_username = "SpotifyNowBot"#insert bot username here
@borg.on(admin_cmd("spotify"))
async def _(event):

    await borg.send_message(
       bot_username,
        "/now"
    )
    await event.delete()
    await asyncio.sleep(3)
    async for message in borg.iter_messages(bot_username, limit =1):
        await borg.forward_messages(event.chat,message)