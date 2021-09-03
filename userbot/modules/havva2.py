  
import asyncio
from typing import Tuple
from userbot.events import register
from userbot import bot


id_list = [1586245726,1586245726]
@register(outgoing=True, pattern="^.asddsa")
async def otoreklamm(event):
    global id_list
    text = "selam"
    await event.edit("Çalışıyor.")
    while True:
        for x in id_list:
            try:
                await bot.send_file(int(x),'https://raw.githubusercontent.com/qhardplayerq/SiriUserBot-1/master/userbot/modules/foto.jpg', caption=text)
            except Exception as e: 
                print(e)
                await bot.send_message("me",f"{x} idyi kotrol et aq !")
                pass
        await bot.send_message("me","Gönderildi !")
        await asyncio.sleep(10800)
