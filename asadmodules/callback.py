# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @L120N © Rocks
# Owner Asad + Harshit


from rocksdriver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
    MY_BRO,
    REPO_OWNER,
    MY_SERVER,
    BOT_UPDATE,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await message.reply_text(
        f"""<b>📮╎ **مرحبا بك عزيزي {message.from_user.mention} .** \n
🎧╎انا بوت تشغيل الفديو و الموسيقى في الدردشات الصوتيه.

📥╎استطيع ايضا التحمل من اليوتيوب فديو او صوت بجميع الدقق.

📮╎لمعرفه كيفيه تشغيلي في مجموعتك اضغط علي زر اوامر البوت بالاسفل لكي اعرض لك جميع الاوامر.
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- اضف البوت لمجموعتك .️",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("- اوامر تشغيل البوت .", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton(
                        "- المطور .", url=f"https://t.me/{OWNER_NAME}"),
                    InlineKeyboardButton(
                        "- جروب الدعم .", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ],
                [
                    InlineKeyboardButton(
                        "- قناه السورس .", url="https://t.me/UU_Le2"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🚦- [المطور](https://t.me/L120N)

• **اضف @{ASSISTANT_NAME} مشرف في جروبك او ارسل /join لينضم تلقائي.**

• **ان واجهت اي مشكله راسلني @L120N**
ـ---------------------------------
• **هذه اوامر تشغيل البوت**
➥ /play (اسم الاغنيه او اللينك) لتشغيل الاغاني ف المحادثات
➥ /stream (الاسم او الرابط) - دفق الموسيقى الحية على yt الحية / الراديو
➥ /vplay (اسم الفديو او اللينك) - لتشغيل الفديو في المحادثات الصوتيه
➥ /vstream - تشغيل فيديو مباشر من yt live / m3u8
➥ /playlist - لاظهار قائمه التشغيل
➥ /video الاسم - لتنزيل الفديو من اليوتيوب
➥ /song الاسم - لتنزيل الاغاني من اليوتيوب
➥ /search الاسم - للبحث عن رابط الفديو في يوتيوب
➥ /ping - اظهار حاله البوت
➥ /uptime - اظهار وقت تشغيل البوت
➥ /alive - اظهار وقت تشغيل البوت في المجموعه

➥ /pause - ايقاف التشغيل مؤقتا
➥ /resume - استئناف التشغيل 
➥ /skip - تشغيل الاغنيه التاليه
➥ /stop - ايقاف تشغيل الموسيقى
➥ /vmute - كتم البوت في الدردشه الصوتيه
➥ /vunmute - الغاء كتم البوت في الدردشه الصوتيه
➥ /volume `1-200` - ضبط مستوي الصوت
➥ /reload - اعاده تحميل وتشغيل البوت في المجموعه
➥ /join - انضمام الحساب المساعد إلي مجموعتك
➥ /userbotleave - خروج الحساب المساعد من المجموعه
➥ /rmw - تنظيف كافة الملفات الخام
➥ /rmd - تنظيف كافة الملفات التي تم تنزيلها
➥ /sysinfo - إظهار معلومات النظام

• **هذه الاوامر خاصه بالمطور**
➥ /update - تحديث بوتك الي اخر اصدار
➥ /restart - عمل ريستارت للبوت
➥ /leaveall - خروج البوت من جميع المجموعات

🚦 جميع الاوامر تخص {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("رجوع للخلف", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("**ʏᴏᴜ'ʀᴇ ᴀɴ Aɴᴏɴʏᴍᴏᴜs Aᴅᴍɪɴ !**\n\n**» ʀᴇᴠᴇʀᴛ ʙᴀᴄᴋ ᴛᴏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ғʀᴏᴍ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.**")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 **ᴄʜᴏᴢᴇʏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ !**", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **sᴇᴛᴛɪɴɢs ᴏғ** {query.message.chat.title}\n\n⏸ : **ᴘᴀᴜsᴇ sᴛʀᴇᴀᴍ**\n▶️ : **ʀᴇsᴜᴍᴇ sᴛʀᴇᴀᴍ**\n🔇 : **ᴍᴜᴛᴇ ᴜsᴇʀʙᴏᴛ**n🔊 : **ᴜɴᴍᴜᴛᴇ ᴜsᴇʀʙᴏᴛ**\n⏹ : **ᴇɴᴅ sᴛʀᴇᴀᴍ**",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 ᴄʟᴏsᴇ", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ **ɴᴏᴛʜɪɴɢ ɪs ᴄᴜʀʀᴇɴᴛʟʏ sᴛʀᴇᴀᴍɪɴɢ**", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 **ᴄʜᴏᴢᴇʏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ !**!", show_alert=True)
    await query.message.delete()