from pyrogram import Client, filters
from config import AUTH_CHANNEL
from pyrogram.types import *
from pyrogram.errors import *

START_TEXT = """**Hello {} 😌
I am a usless Bot**

>> `I can generate text to QR Code with QR Code decode to text support.`"""

buttons = [[
                InlineKeyboardButton('↖️ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘs ↗️', url=f'http://t.me/tedzo_bot?startgroup=true')
                ],[
                InlineKeyboardButton('🧞‍♀️ Sᴇᴀʀᴄʜ', switch_inline_query_current_chat=''),
                InlineKeyboardButton('🔍 Gʀᴏᴜᴘ', url=f'https://t.me/tedzomovie01')
                ],[
                InlineKeyboardButton('🙆🏻 Hᴇʟᴘ ', callback_data='help'),
                InlineKeyboardButton('🎁 Hᴇʟᴘ++', callback_data='home'),
                ],[
                InlineKeyboardButton('⚙ Sᴇᴛᴛɪɴɢs', callback_data='close'),
                InlineKeyboardButton('♥️ Aʙᴏᴜᴛ', callback_data='about')
                ],[
                InlineKeyboardButton('⪦ BOT ⪧', url='https://t.me/tedzo_bot')
                ],[
                InlineKeyboardButton('🎉 Learn BOT making 🎊', url="https://youtube.com/@mrbeast")
                ]]

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

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
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
    await message.reply_text(
        text=START_TEXT.format(message.from_user.mention),
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
