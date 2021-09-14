import asyncio
from typing import Tuple
from userbot.events import register
from userbot import bot


@register(outgoing=True, pattern="^.kanalım")
async def mesaj(event):
    await event.edit("**👑Kanal Linkimiz👑**👇\nhttps://t.me/joinchat/V5uno4h5L43QKN9o")
