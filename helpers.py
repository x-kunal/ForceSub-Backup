# (C) KD Botz 

# June 8th 2022

import asyncio
from info import DB_CHANNEL, FSUB_CHANNEL, CHANNEL_LINK, LIST
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton

async def copy_msg(msg):
    file = msg.document or msg.video
    name = file.file_name.split(".")[-1]
    if name in LIST: 
       return
    else:
       try:
           await msg.copy(DB_CHANNEL)
       except FloodWait as e:
           await asyncio.sleep(e.x)
           await msg.copy(DB_CHANNEL)

async def force_sub(bot, msg):
       try:
          member = await bot.get_chat_member(FSUB_CHANNEL, msg.from_user.id)
          if member.status == "banned":
            await msg.reply(f"𝖲ᴏʀʀʏ {msg.from_user.mention} !\n\n𝖸ᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ, ʏᴏᴜ ᴡɪʟʟ ʙᴇ ʙᴀɴɴᴇᴅ ғʀᴏᴍ ʜᴇʀᴇ ᴡɪᴛʜɪɴ 𝟷𝟶 𝗌ᴇᴄᴏɴᴅ𝗌")
            await asyncio.sleep(10)
            await bot.ban_chat_member(msg.chat.id, msg.from_user.id)
       except UserNotParticipant:
            await bot.restrict_chat_member(chat_id=msg.chat.id, 
                                           user_id=msg.from_user.id,
                                           permissions=ChatPermissions(can_send_messages=False)
                                           )
            await msg.reply(f"<b>𝖧ᴇʟʟᴏ {msg.from_user.mention} !</b>\n\n<b>𝖸ᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ ɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍᴇ𝗌𝗌ᴀɢᴇ ʜᴇʀᴇ</b>\n\n<b>𝖠ғᴛᴇʀ ᴊᴏɪɴɪɴɢ ᴄʟɪᴄᴋ ᴏɴ ᴛʀʏ ᴀɢᴀɪɴ</b>", 
                            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Jᴏɪɴ Cʜᴀɴɴᴇʟ", url=CHANNEL_LINK)],
                                                               [InlineKeyboardButton("Tʀʏ Aɢᴀɪɴ", callback_data="checksub")]])
                            )
       except Exception as e:
            print(e)

async def auto_delete(Bot, msg):
    chat, msg_id = msg.chat.id, msg.message_id
    try:       
       await asyncio.sleep(600) # not tested, edit if you need
       await Bot.delete_messages(chat, msg_id)
    except Exception as e:
       print(e)

async def check_fsub(bot, update):
    try:
       user=update.message.reply_to_message.from_user.id
    except:
       user=update.from_user.id
    if update.from_user.id==user:
       try:
          member = await bot.get_chat_member(FSUB_CHANNEL, user)          
       except UserNotParticipant:
          await update.answer("𝖨 𝖫ɪᴋᴇ 𝖸ᴏᴜʀ 𝖲ᴍᴀʀᴛɴᴇ𝗌𝗌 𝖡ᴜᴛ 𝖣ᴏɴ'ᴛ ʙᴇ 𝖮ᴠᴇʀ 𝖲ᴍᴀʀᴛ 😏", show_alert=True)
       except Exception as e:
            print(e)
       else:
           await bot.restrict_chat_member(chat_id=update.message.chat.id, 
                                          user_id=user,
                                          permissions=ChatPermissions(can_send_messages=True,
                                                                      can_send_media_messages=True,
                                                                      can_send_other_messages=True)
                                          )
           await update.message.edit(f"𝖧ᴇʟʟᴏ {update.from_user.mention} !\n\n𝖶ᴇʟᴄᴏᴍᴇ ᴛᴏ {update.message.chat.title}")
    else:
       await update.answer("𝖳ʜᴀᴛ'𝗌 ɴᴏᴛ ғᴏʀ ʏᴏᴜ ʙʀᴜʜ 😂", show_alert=True)
 
# Kangers stay away 😒
