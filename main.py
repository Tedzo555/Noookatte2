import os
from pyrogram import Client, filters
import asyncio
API_ID = '15453419'
API_HASH = '6c9c9e5a2e65daf192e7dd9dde026f45'
BOT_TOKEN = '7324179073:AAHpYAvt95Q7q2EJwOU6uAlEc67_aTReB4Q'


app = Client(
    "mybot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root="plugins")
)
