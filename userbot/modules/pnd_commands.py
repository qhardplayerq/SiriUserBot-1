import asyncio
from typing import Tuple
from userbot.events import register
from userbot import bot

@register(outgoing=True, pattern="^.kontrol")
async def mesaj(event):
    await event.edit("**Çalışıyor**")
    
@register(outgoing=True, pattern="^.kad")
async def mesaj(event):
    await event.edit("Kullanıcı adınızı ana menüdeki sol taraftaki referans bölümünden bulabilirsiniz. Referans linkinizin / işaretinden sonraki sizin kullanıcı adınızdır.\n\nÖrnek:\nwww.pnd. tl/ref/ali    (kullanıcı adı: ali) ")

@register(outgoing=True, pattern="^.22cpm")
async def mesaj(event):
    await event.edit("22TL CPM almak için aşşağıdaki kayıt linkinden kaydolup kullanıcı adınızı @admin etiketi ile gruba atmanız gerekmektedir, eğer kaydınız varsa yine aynı şekilde @admin etiketi ile gruba atmanız gerekmektedir. CPM panelinize gün içinde tanımlanır, tanımlanınca bir yönetici sizinle iletişime geçecektir...\n\nKayıt Linki: https://www.pnd.tl/auth/signup")

@register(outgoing=True, pattern="^.kaydol")
async def mesaj(event):
    await event.edit("1.Adım: www.pnd.tl/ref/Ademko bu linke tıkla.\n2.Adım: Sağ üstteki üç çizgiden 'KAYDOL' yazısına tıkla ve kaydol.\n3.Adım: Kullanıcı adını telegram grubumuza @admin etiketi ile yöneticilere ilet.") 

@register(outgoing=True, pattern="^.deneme")
async def mesaj(event):
    await event.edit("**Deneme Kısa Linkimiz👇**\nhttps://pnds.live/denemelink")

@register(outgoing=True, pattern="^.ödeme")
async def mesaj(event):
    await event.edit("**PND.TL ÖDEME LİMİTLERİ VE TARİHLERİ**\n\n**Papara** Alt Limit 50TL'dir.\n**Banka ve İninal** Alt Limit 15TL'dir.\n**Bitcoin** Alt Limit 100TL'dir.\n**Dogecoin** Alt Limit 150TL'dir.\n\nPapara: Günlük ödeme.\nBitcoin: Günlük ödeme.\nDogecoin: Günlük ödeme.\nBanka ve İninal: Her Ayın 1-11-21'nde\n\n\n**DİKKAT**👇⚠️\nBanka ve İninal için ayın 1-11-21 inde yapılan çekim talepleri bir sonraki ödeme tarihinde yapılacaktır.")
 
@register(outgoing=True, pattern="^.api")
async def mesaj(event):
    resim ='https://raw.githubusercontent.com/qhardplayerq/SiriUserBot-1/master/userbot/modules/api.JPG' 
    text="APİ adresimize sol taraftaki menü çubuğundaki **Araçlar** sekmesinden **Geliştirici API** bölümünden yeşil kutunun içinde bulabilirsiniz..."
    await event.client.send_file(event.chat_id, file=resim, caption=text)
