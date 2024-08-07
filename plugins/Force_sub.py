from pyrogram import Client, filters, enums
import random
from config import AUTH_CHANNEL, PICS
from pyrogram.types import *
from pyrogram.errors import *

START_TXT = """<b>Hᴇʟʟᴏ {},ᴍʏ ɴᴀᴍᴇ {}⚡\nɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ...!\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ....!\nᴘᴏᴡᴇʀᴇᴅ ʙʏ - @tedzo01</b>"""

async def is_subscribed(bot, query, channel):
    btn = []
    for id in channel:
        chat = await bot.get_chat(int(id))
        try:
            await bot.get_chat_member(id, query.from_user.id)
        except UserNotParticipant:
            btn.append([InlineKeyboardButton(f'Join {chat.title}', url=chat.invite_link)])
        except Exception as e:
            pass
    return btn

@Client.on_message(filters.command("start")) 
async def start_message(bot, message):
    if AUTH_CHANNEL:
        try:
            btn = await is_subscribed(client, message, AUTH_CHANNEL)
            if btn:
                username = (await client.get_me()).username
                if message.command[1]:
                    btn.append([InlineKeyboardButton("♻️ Try Again ♻️", url=f"https://t.me/{username}?start={message.command[1]}")])
                else:
                    btn.append([InlineKeyboardButton("♻️ Try Again ♻️", url=f"https://t.me/{username}?start=true")])
                await message.reply_text(text=f"<b>👋 Hello {message.from_user.mention},\n\nPlease join the channel then click on try again button. 😇</b>", reply_markup=InlineKeyboardMarkup(btn))
                return
        except Exception as e:
            print(e)
            buttons = [[
            InlineKeyboardButton('• ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ •', url='https://t.me/SA_Bots')
            ],[
            InlineKeyboardButton('• ᴍᴏᴠɪᴇs ᴄʜᴀɴɴᴇʟ', url='https://t.me/+ohjofBYY5KljZTdl'),
            InlineKeyboardButton('ᴍᴏᴠɪᴇs ɢʀᴏᴜᴘ •', url='https://t.me/+RJ5z0YIRewsxYWNl')
            ],[
            InlineKeyboardButton('• ᴄʀᴇᴀᴛᴇ ʏᴏᴜʀ ᴏᴡɴ ᴄʟᴏɴᴇ ʙᴏᴛ •', url='https://t.me/+ohjofBYY5KljZTdl')
            ],[
            InlineKeyboardButton('• ʜᴇʟᴘ', url='https://t.me/+ohjofBYY5KljZTdl'),
            InlineKeyboardButton('ᴀʙᴏᴜᴛ •', url='https://t.me/+ohjofBYY5KljZTdl')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        me2 = (await client.get_me()).mention
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=START_TXT.format(message.from_user.mention, me2),
            reply_markup=reply_markup
)
