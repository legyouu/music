# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @L120N © Rocks
# Owner Asad + Harshit
 

from cache.admins import admins
from rocksdriver.asad import call_py
from pyrogram import Client, filters
from rocksdriver.decorators import authorized_users_only
from rocksdriver.filters import command, other_filters
from rocksdriver.queues import QUEUE, clear_queue
from rocksdriver.utils import skip_current_song, skip_item
from config import BOT_USERNAME, GROUP_SUPPORT, IMG_3, UPDATES_CHANNEL, REPO_OWNER, BOT_UPDATE, MY_BRO, MY_SERVER, BOT_NAME, MY_HEART
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


bttn = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 ɢᴏ ʙᴀᴄᴋ", callback_data="cbmenu")]]
)


bcl = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🗑 ᴄʟᴏsᴇ", callback_data="cls")]]
)


@Client.on_message(command(["reload", f"reload@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(f"""**━━━━━━━━━━━━━━━━━━━
🎧╎انا بوت تشغيل الفديو و الموسيقى في الدردشات الصوتيه.

📥╎استطيع ايضا التحمل من اليوتيوب فديو او صوت بجميع الدقق.
━━━━━━━━━━━━━━━━━━━**""",
    )


@Client.on_message(command(["skip", f"skip@{BOT_USERNAME}", "vskip"]) & other_filters)
@authorized_users_only
async def skip(client, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- LeGenD .️", url=f"https://t.me/L120N"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/UU_Le2"),
            ]
        ]
    )

    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("❌ **ᴀᴛ [playing music](t.me/L120N) Nothing is currently playing**")
        elif op == 1:
            await m.reply("✅ __Queues__ **ɪs ᴇᴍᴘᴛʏ.**\n\n**• Stopped [playing music](t.me/UU_Le2) Userbot leaving voice chat**")
        elif op == 2:
            await m.reply("🗑️ **Clearing the queues**\n\n**Stopped [playing music](t.me/UU_Le2) Userbot leaving voice chat**")
        else:
            await m.reply_photo(
                photo=f"{IMG_3}",
                caption=f"⏭ **Skipped to next tarck.**\n\n🎙️ **Name:** [{op[0]}]({op[1]})\n\n🔋 **Status:** `Playing`\n🎧 **Request by:** {m.from_user.mention()}",
                reply_markup=keyboard,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "🗑 **sᴏɴɢ ʀᴇᴍᴏᴠᴇᴅ**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(
    command(["stop", f"stop@{BOT_USERNAME}", "end", f"end@{BOT_USERNAME}", "vstop"])
    & other_filters
)
@authorized_users_only
async def stop(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("✅ **Stopped** [playing music](t.me/L120N) **in the group**")
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- LeGenD .️", url=f"https://t.me/L120N"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/UU_Le2"),
            ]
        ]
    )
        except Exception as e:
            await m.reply(f"🚫 **Eʀʀᴏʀr:**\n\n`{e}`")
    else:
        await m.reply("❌ **ᴀᴛ** [playing music](t.me/UU_Le2) **Nothing is streaming**")
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- LeGenD .️", url=f"https://t.me/L120N"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/UU_Le2"),
            ]
        ]
    )


@Client.on_message(
    command(["pause", f"pause@{BOT_USERNAME}", "vpause"]) & other_filters
)
@authorized_users_only
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                "⏸ **Tʀᴀᴄᴋᴇ ᴘᴀᴜsᴇᴅ.**\n\n• **Tᴏ ʀᴇsᴜᴍᴇ ᴜsᴇ ᴛʜᴇ**\n» /resume **ᴄᴏᴍᴍᴀɴᴅ**."
            )
        except Exception as e:
            await m.reply(f"🚫 **Eʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ᴀᴛ** [playing music](t.me/UU_Le2) **Nothing is streaming**")


@Client.on_message(
    command(["resume", f"resume@{BOT_USERNAME}", "vresume"]) & other_filters
)
@authorized_users_only
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                "▶️ **ᴀᴛ** [playing music](t.me/UU_Le2) **Tʀᴀᴄᴋ ɪs ʀᴇsᴜᴍᴇᴅ.**\n\n• **To pause the stream, use the**\n» /pause command."
            )
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- LeGenD .️", url=f"https://t.me/L120N"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/UU_Le2"),
            ]
        ]
    )
        except Exception as e:
            await m.reply(f"🚫 **Error:**\n\n`{e}`")
    else:
        await m.reply("❌ **ᴀᴛ** [playing music](t.me/UU_Le2) **Nothing is streaming**")
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- LeGenD .️", url=f"https://t.me/L120N"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/UU_Le2"),
            ]
        ]
    )


@Client.on_message(
    command(["mute", f"mute@{BOT_USERNAME}", "vmute"]) & other_filters
)
@authorized_users_only
async def mute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await m.reply(
                "🔇 **ᴀᴛ** [playing music](t.me/L120N) **ᴜsᴇʀʙᴏᴛ ɪs ᴍᴜᴛᴇᴅ.**\n\n• **Tᴏ ᴜɴᴍᴜᴛᴇ ᴛʜᴇ ᴜsᴇʀʙᴏᴛ, ᴜsᴇ ᴛʜᴇ**\n» /unmute **ᴄᴏᴍᴍᴀɴᴅ**."
            )
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- LeGenD .️", url=f"https://t.me/L120N"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/UU_Le2"),
            ]
        ]
    )
        except Exception as e:
            await m.reply(f"🚫 **Eʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ᴀᴛ** [playing music](t.me/UU_Le2) **Nothing is streaming**")
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- LeGenD .️", url=f"https://t.me/L120N"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/UU_Le2"),
            ]
        ]
    )


@Client.on_message(
    command(["unmute", f"unmute@{BOT_USERNAME}", "vunmute"]) & other_filters
)
@authorized_users_only
async def unmute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await m.reply(
                "🔊 **ᴀᴛ** [playing music](t.me/UU_Le2) **ᴜsᴇʀʙᴏᴛ ɪs ᴜɴᴍᴜᴛᴇᴅ.**\n\n• **ᴛᴏ ᴍᴜᴛᴇ ᴛʜᴇ ᴜsᴇʀʙᴏᴛ ᴜsᴇ ᴛʜᴀ**\n» /mute **ᴄᴏᴍᴍᴀɴᴅ**."
            )
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- LeGenD .️", url=f"https://t.me/L120N"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/UU_Le2"),
            ]
        ]
    )
        except Exception as e:
            await m.reply(f"🚫 **Eʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **ᴀᴛ** [playing music](t.me/UU_Le2) **Nothing is streaming**")
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- LeGenD .️", url=f"https://t.me/L120N"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/UU_Le2"),
            ]
        ]
    )


@Client.on_callback_query(filters.regex("cbpause"))
async def cbpause(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("🔋 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await query.edit_message_text(
                "⏸ the streaming has paused", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ Nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cbresume"))
async def cbresume(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("🔋 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await query.edit_message_text(
                "▶️ the streaming has resumed", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ Nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cbstop"))
async def cbstop(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("🔋 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await query.edit_message_text("✅ **this streaming has ended**", reply_markup=bcl)
        except Exception as e:
            await query.edit_message_text(f"🚫 **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ Nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cbmute"))
async def cbmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("🔋 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await query.edit_message_text(
                "🔇 userbot succesfully muted", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ Nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cbunmute"))
async def cbunmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("🔋 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await query.edit_message_text(
                "🔊 Userbot Successfully unmutd**", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **Error:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ **ɴᴏᴛʜɪɴɢ ɪs ᴄᴜʀᴇɴᴛʟʏ sᴛʀᴇᴀᴍɪɴɢ**", show_alert=True)


@Client.on_message(
    command(["volume", f"volume@{BOT_USERNAME}", "vol"]) & other_filters
)
@authorized_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.change_volume_call(chat_id, volume=int(range))
            await m.reply(
                f"✅ **Volume set to** `{range}`%"
            )
        except Exception as e:
            await m.reply(f"🚫 **Error:**\n\n`{e}`")
    else:
        await m.reply("❌ **Nothing is streaming**")