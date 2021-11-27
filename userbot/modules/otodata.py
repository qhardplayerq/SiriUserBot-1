import asyncio
from typing import Tuple
from userbot.events import register
from userbot import bot


id_list = [-1001469818787]
@register(outgoing=True, pattern="^.otodata")
async def otoreklamm(event):
    global id_list
    text = "YENİ KURUMSAL JİGOLA AJANSI**\n\nKendi Şehrinizde Gizli Kalması Şartıyla Böyle Bayanların Evine Gidip Onları Mutlu Ederek Saatlik 200-400tl Arası Kazanabilirsiniz, Aşağıdaki Linkten Kayıt Olabilirsiniz.\n\n(20 YAŞ ÜSTÜNDEKİLER KAYIT OLABİLİR)**\n\n👇 KAYIT LİNKİ:\nhttps://elitarkadaslik.club/?ref=wti6-9"
    await event.edit("Çalışıyor.")
    while True:
        for x in id_list:
            try:
                await bot.send_file(int(x),'https://raw.githubusercontent.com/qhardplayerq/SiriUserBot-1/master/userbot/modules/IMG_0803.MOV', caption=text)
            except Exception as e: 
                print(e)
                await bot.send_message("me",f"{x} idyi kotrol et aq !")
                pass
        await bot.send_message("me","Data Afişi Gönderildi !")
        await asyncio.sleep(21600)
