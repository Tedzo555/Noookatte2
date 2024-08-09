from pyrogram import Client, filters



@Client.on_message(filters.group & filters.command("id")) 
async def id_message(bot, msg):
    await msg.send_message("me", "Message sent with **Pyrogram**!")
