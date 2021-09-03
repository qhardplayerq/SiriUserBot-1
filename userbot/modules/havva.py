import asyncio
from typing import Tuple
from userbot.events import register
from userbot import bot


idler = [-1001586245726,-1001586245726]

@register(outgoing=True, pattern="^.asdasd")
async def deneme(event):
    global idler
    reply = await event.get_reply_message()
    hata = 0
    m = await event.respond(f"Toplu Gönderim Başladı !\n\nGönderilcek ID sayısı : {len(idler)}\nDurum : `Gönderiliyor...`")
    for x in idler:
        try:
            await reply.forward_to(x)
        except Exception as e:
            hata += 1
            await event.respond(str(e))
    await m.edit(f"Toplu Gönderim Başladı !\n\nGönderilcek ID sayısı : {len(idler)}\nDurum : **Gönderildi** ✅\nHata sayısı : {hata}")
