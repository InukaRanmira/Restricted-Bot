import os
from .. import bot as Drone
from telethon import events, Button

from ethon.mystarts import start_srb
    
S = '/' + 's' + 't' + 'a' + 'r' + 't'

@Drone.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):    
    Drone = event.client                    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Temporary thumbnail saved!")
        
@Drone.on_message(filters.command("start"))
async def startprivate(client, message):
    if await forcesub(client, message):
       return
    #return
    chat_id = message.from_user.id
    if not await db.is_user_exist(chat_id):
    file_id = "CAACAgUAAxkBAAEHlRdj3irNZYBJdsijeOXh2WPOCz1LBAACUQkAAktIQFYewZtYpX7fFy4E"
    await client.send_sticker(message.chat.id, file_id, reply_markup=start_menu)
    text = f"Hi {message.from_user.mention}, 👋 Hello {message.from_user.first_name}\n\nI am Save Restricted Contents Bot, I can save files of restricted channels as well as group.
\n\n\n\nFOR PUBLIC CHATS\n\n> just send post/s link\n\nFOR PRIVATE CHATS\n\n> First send invite link of the chat\n\n> Then send post/s link\n\nPowered By SMΛЯT TΞϾH 🇱🇰(https://t.me/+c8oBVEKPAD84ZGY1)"
    reply_markup = START_BUTTON  
    await message.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )
    
