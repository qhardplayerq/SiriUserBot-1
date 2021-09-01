#Pharex
from userbot import CMD_HELP
from userbot.events import register
from userbot.cmdhelp import CmdHelp

kanallar = [-1001285905728, -1001469818787, -1001275030556, -1001188302270, -1001151369031]

@register(pattern="^.post")
async def postitf(message):
    yanitlanan_mesaj = message.get_reply_message()
    count = 0
    await message.edit("`Post gönderiliyor...`")
    for kanal in kanallar:
        try:
            await message.client.send_file(kanal, file=yanitlanan_mesaj.media, caption=yanitlanan_mesaj.text)
        except Exception as e:
            await message.reply(f"Bir kanala post gönderilemedi!\n\n{e}\n\n{kanal}")
        else:
            count += 1
    await message.edit(f"{count} `kanala post gönderildi.`")