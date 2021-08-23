import asyncio
from typing import Tuple
from userbot.events import register
from userbot import bot


@register(outgoing=True, pattern="^.odeme")
async def mesaj(event):
    await event.edit("**PND.TL ÖDEME LİMİTLERİ VE TARİHLERİ**\n\n**Papara** Alt Limit 50TL'dir.\n**Banka ve İninal** Alt Limit 15TL'dir.\n**Bitcoin** Alt Limit 100TL'dir.\n**Dogecoin** Alt Limit 150TL'dir.\n\nPapara: Günlük ödeme.\nBitcoin: Günlük ödeme.\nDogecoin: Günlük ödeme.\nBanka ve İninal: Her Ayın 1-11-21'nde\n\n\n**DİKKAT**👇⚠️\nBanka ve İninal için ayın 1-11-21 inde yapılan çekim talepleri bir sonraki ödeme tarihinde yapılacaktır.")
