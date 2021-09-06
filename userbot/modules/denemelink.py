import asyncio
from typing import Tuple
from userbot.events import register
from userbot import bot


@register(outgoing=True, pattern="^.deneme")
async def mesaj(event):
    await event.edit("**Deneme Kısa Linkimiz 👇\nhttps://pnds.live/denemelink**")
