from pyrogram import Client, filters
from pyrogarm import types.messege
import asyncio


@Client.on_message(filters.group & filters.command("start")) 
async def id_message(bot, msg):
    await msg.send_reaction(chat_id, message_id=message_id, emoji="🔥")
