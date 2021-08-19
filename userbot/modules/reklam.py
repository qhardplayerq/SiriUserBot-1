import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
from telethon import events
from datetime import datetime
from userbot.util import admin_cmd
from userbot import bot


@bot.on(admin_cmd(pattern="reklam"))
async def _(event):
    await event.delete()
    for a in range(1,2):
        await bot.send_message(
            event.chat_id,
            "REKLAM SEÇENEKLERİMİZ:\n=========================\n25K KANAL👇\n6 saat 40TL (3 saat ön plan sonra sabit)\n12 saat 60TL (5 saat ön plan sonra sabit)\n24 saat 90TL (10 saat ön plan sonra sabit)\n\n50K KANAL👇\n6 saat 80TL (3 saat ön plan sonra sabit)\n12 saat 150TL (5 saat ön plan sonra sabit)\n24 saat 250TL (10 saat ön plan sonra sabit)\n\n125K KİTLE👇\n6 saat 120TL (3 saat ön plan sonra sabit)\n12 saat 200TL (5 saat ön plan sonra sabit)\n24 saat 350TL (10 saat ön plan sonra sabit)\n========================="
        )
