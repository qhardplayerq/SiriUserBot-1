import asyncio
from typing import Tuple
from userbot.events import register
from userbot import bot


idler = [1586245726,1586245726]

@register(outgoing=True, pattern="^.asdasd")
async def deneme(event):
    global idler
    reply = await event.get_reply_message()
    hata = 0
    m = await event.respond(f"Toplu Gönderim B aşladı !\n\nGönderilcek ID sayısı : {len(idler)}\nDurum : `Gönderiliyor...`")
    for x in idler:
            try:
                await bot.send_message(x,reply.message)
            except:
                hata += 1
                pass    
    await bot.edit_message(event.chat_id,m,f"Toplu Gönderim Başladı !\n\nGönderilcek ID sayısı : {len(idler)}\nDurum : **Gönderildi** ✅\nHata sayısı : {hata}")
