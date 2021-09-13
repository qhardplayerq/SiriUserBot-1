import asyncio
from typing import Tuple
from userbot.events import register
from userbot import bot


@register(outgoing=True, pattern="^.reklam")
async def mesaj(event):
    await event.edit("24 Saat Sabite Alınacak Post 150₺\n12 Saat Sabite Alınacak Post 80₺\n\n24 Saat Duracak Post 100₺\n12 Saat Duracak Post 60₺\n\n__1 Hafta 700₺ 7/24 Sabite Hergün İstediğiniz Saate Reklam Silinip Tekrar Paylaşılacaktır (00.00-01.00) harici__\n\nPost Altı Reklam En Az Alım 1 Hafta 400₺ Uzun Vadeli Anlaşmalarda Fiyat Pazarlığı Yapılır Aylık Anlaşma Söz Konusu İse Her İçeriğimizde Ableminiz Ve Kanalınza Ulaşa Bilcekleri Bağlantılar Paylaşılır\n\n__Her Postun Altında 2. Kanalımız Gibi Abonelere Takdim Edilerek Reklam Yapılır__\n\n**ÖRNEK👇**\n====================\n🌟 Liseli Kuzenini ayakta sikiyor. 🔞\n\n📛 SESİ AÇ 'a tıklamayı unutma\n\n👇DEVAMI LİNKTE👇\n\n**LİNK**🔗 https://pnds.live/ZPPQ0R\n\nYedek Kanalımız 👉 @Reklamınız\n\n❗️Link nasıl açılır\n👉 https://t.me/linkk_gecmee\n====================\n\nReklam Aşağıda Belirtilen Kanalda Yapılacaktır.\n\n👑Kanal Linkimiz👑\nhttps://t.me/joinchat/V5uno4h5L43QKN9o")
