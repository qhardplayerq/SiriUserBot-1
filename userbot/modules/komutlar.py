import asyncio
from typing import Tuple
from userbot.events import register
from userbot import bot


@register(outgoing=True, pattern="^.komutlar")
async def mesaj(event):
    await event.edit("**EKLENEN KOMUTLAR**\\kanallar\notoreklam\notopnd\notocpm") 
