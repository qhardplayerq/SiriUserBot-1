import asyncio
from typing import Tuple
from userbot.events import register
from userbot import bot


@register(outgoing=True, pattern="^.papara")
async def mesaj(event):
    await event.edit("**PAPARA Adresim**👇\n1487349446")
