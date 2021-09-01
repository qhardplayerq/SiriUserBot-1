import asyncio
from typing import Tuple
from userbot.events import register
from userbot import bot


@register(outgoing=True, pattern="^.ID")
async def mesaj(event):
    resim ='https://raw.githubusercontent.com/qhardplayerq/SiriUserBot-1/master/userbot/modules/ID.PNG'
    text="Ödeme ID mizi öğrenmek için sol taraftaki menülerden **PARA ÇEK** menüsüne giriyoruz. Sonra resimdeki yuvarlak içinde gösterilen **ID** yi @admin etiketi ile gruba veya yetkili birine iletiyoruz. Bol Kazançlar. "
    await event.client.send_file(event.chat_id, file=resim, caption=text) 
