import os
import time
from pyrogram import Client, filters
import random
import asyncio
API_ID = '15453419'
API_HASH = '6c9c9e5a2e65daf192e7dd9dde026f45'
BOT_TOKEN = '7384862816:AAEMz0He5W6iTRN-SLf3gM5-PhtFe8wx31s'
# Define a list of prank messages

app = Client(
    "mybot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root="plugins")
)
