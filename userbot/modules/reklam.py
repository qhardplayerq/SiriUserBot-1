from typing import Pattern
from telethon import TelegramClient,events 

@bot.on(events.NewMessage(pattern='^(?i)kontrol$'))
async def deneme (event):
    global deneme_m
    await event.reply("Çalışıyor...")
