#hyyy
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import *
from random import choice

START_TEXT = """**Hello {} 😌
I am a usless Bot**

>> `I can generate text to QR Code with QR Code decode to text support.`"""

buttons = [[
                InlineKeyboardButton('↖️ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘs ↗️', url=f'http://t.me/{message.username}?startgroup=true')
                ],[
                InlineKeyboardButton('🧞‍♀️ Sᴇᴀʀᴄʜ', switch_inline_query_current_chat=''),
                InlineKeyboardButton('🔍 Gʀᴏᴜᴘ', url=f'https://t.me/{MOVIE_GROUP_USERNAME}')
                ],[
                InlineKeyboardButton('🙆🏻 Hᴇʟᴘ ', callback_data='help'),
                InlineKeyboardButton('🎁 Hᴇʟᴘ++', callback_data='leech_url_help'),
                ],[
                InlineKeyboardButton('⚙ Sᴇᴛᴛɪɴɢs', callback_data='openSettings'),
                InlineKeyboardButton('♥️ Aʙᴏᴜᴛ', callback_data='about')
                ],[
                InlineKeyboardButton('⪦ 𝕄𝕆𝕍𝕀𝔼 ℂℍ𝔸ℕℕ𝔼𝕃 ⪧', url='https://t.me/real_MoviesAdda3')
                ],[
                InlineKeyboardButton('🎉 Learn BOT making 🎊', url="https://youtube.com/@LazyDeveloperr")
                ]]

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
      	reply_markup=buttons,
      	quote=True
    )
@Client.on_callback_query()
async def cb_data(bot, update):
    
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=buttons
        )
    elif update.data == "close":
        await update.answer("Closed")
        await update.message.delete()

    elif update.data == "help":
        await update.message.edit_text(
            text=START_TEXT,
            disable_web_page_preview=True,
            reply_markup=buttons
        )
    
    elif update.data == "about":
        await update.message.edit_text(
            text=START_TEXT,
            disable_web_page_preview=True,
            reply_markup=buttons
        )
    
    else:
        await update.message.delete()

  
