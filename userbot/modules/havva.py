import asyncio
from typing import Tuple
from userbot.events import register
from userbot import bot


idler = [-1001586245726,-1001052096636]

@register(outgoing=True, pattern="^.havva")
async def deneme(event):
    global idler
    reply = await event.get_reply_message()
    hata = 0
    m = await event.respond(f"Toplu Gönderim Başladı !\n\nGönderilcek ID sayısı : {len(idler)}\nDurum : `Gönderiliyor...`")
    for x in idler:
            try:
                await bot.send_message(x,reply.message)
            except:
                hata += 1
                pass    
    await bot.edit_message(event.chat.id,m,f"Toplu Gönderim Başladı !\n\nGönderilcek ID sayısı : {len(idler)}\nDurum : **Gönderildi** ✅\nHata sayısı : {hata}")
