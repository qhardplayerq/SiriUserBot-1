import asyncio
from typing import Tuple
from userbot.events import register
from userbot import bot


id_list = [1275989066,1435523233,1276667828,1399376603,1377871517,1559899893,1328224261,1476898506,1254179689,1226168546,1245244239,1583615217,1463683383,1338215425,1224401851]
@register(outgoing=True, pattern="^.otoreklam")
async def otoreklamm(event):
    global id_list
    text = "SAĞLAM SİSTEMİMİZ İLE ASLA SİZİ ÜZMÜYORUZ..\n\nSizde tıklanmalarınız eksik sayılmasına engel olmak ve 22TL CPM ile kazancına kazanç katmak için yapman gereken tek şey PND.TL ye gelmek\n\n[👉PND.TL TELEGRAM GRUBUMUZ İÇİN TIKLA👈](https://t.me/joinchat/QXzIKZw5BV5mMmJk)"
    while True:
        for x in id_list:
            try:
                await bot.send_file(x,'pndlogo.png', caption=text)
            except:
                await bot.send_message("me",f"{x} idyi kotrol et aq !")
                pass
        await asyncio.sleep(7200)

