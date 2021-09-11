import json
import logging
import requests
# import aiohttp
import asyncio
from userbot import bot
from userbot.util import admin_cmd
from urllib.request import Request, urlopen
WEB_HDRS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Accept': 'text/html,text/plain,application/xhtml+xml,application/xml,application/_json;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Charset': 'Windows-1252,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8;q=0.5',
    'Connection': 'keep-alive'
}
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
logger = logging.getLogger(__name__)

 
@bot.on(admin_cmd(pattern=("ks ?(.*)")))
async def get_adzan(event):
  link = event.pattern_match.group(1).split('http')
  
  print(link)
  if link:
        url = f"https://www.pnd.tl/api?api=90edf199f17aa2f2455d8d624cc524a097627291&url=http{link[1]}&category=6"

        ksl = requests.get(url).json()
        ksl = ksl['shortenedUrl']
        #await event.edit(f"{link[1]}\n\n❌ SILINMEDEN IZLE ❌\n\n👉 {ksl}\n\nLink nasıl açılır\n👉@linkk_gecmee")
        await event.edit(f"{link[0]}\n\n👇DEVAMI LİNKTE👇\n\n𝐋𝐢𝐍𝐊🔗 {ksl}")
