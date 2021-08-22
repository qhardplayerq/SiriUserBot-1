import asyncio
from typing import Tuple
from userbot.events import register
from userbot import bot


id_list = [-1001275989066,-1001435523233,-1001276667828,-1001399376603,-1001377871517,-1001559899893,-1001328224261,-1001476898506,-1001254179689,-1001226168546,-1001245244239,-1001583615217,-1001463683383,-1001338215425,-1001224401851,-1001561556131]
@register(outgoing=True, pattern="^.otoreklam")
async def otoreklamm(event):
    global id_list
    text = "EN ÇOK TIKLANAN LİNKLERİ SİZİN İÇİN TOPLUYORUZ VE YANDEX OLARAK PAYLAŞIYORUZ💰 SEN DE BİZİ KULLAN FARKI ANLA😎\n\nKAYNAK 11\n\nOtoposter Link: https://telegram.me/OtoPosterBot?start=Kaynak11\n\n[Kaynak Kanalına Katılmak İçin Tıkla: https://t.me/joinchat/SHx3F18jtKk4ZWEx](https://t.me/joinchat/SHx3F18jtKk4ZWEx)"
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
        await asyncio.sleep(7200)
