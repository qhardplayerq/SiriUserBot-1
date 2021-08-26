import asyncio
from typing import Tuple
from userbot.events import register
from userbot import bot


idler = [-1001275989066,-1001435523233,-1001276667828,-1001399376603,-1001377871517,-1001559899893,-1001328224261,-1001476898506,-1001254179689,-1001226168546,-1001245244239,-1001583615217,-1001463683383,-1001338215425,-1001224401851,-1001561556131]

@register(outgoing=True, pattern="^.gonder")
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