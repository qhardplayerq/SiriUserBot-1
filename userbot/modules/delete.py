import asyncio
from typing import Tuple
from userbot.events import register
from userbot import bot


@register(outgoing=True, pattern="^.sil")
async def mesaj(event):
    yanitlanan_mesaj = await event.get_reply_message()
    await yanitlanan_mesaj.delete()
