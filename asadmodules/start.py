# A Powerful Music Bot Property Of Muslim Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# @L120N 
# Owner LEGEND






from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
    REPO_OWNER,
    MY_BRO,
    MY_SERVER,
    BOT_UPDATE,
)
from asadmodules import __version__
from rocksdriver.asad import user
from rocksdriver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


# Roses are red, Violets are blue, A face like yours, Belongs in a zoo.

@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>๐ฎโ **ูุฑุญุจุง ุจู ุนุฒูุฒู {message.from_user.mention} .** \n
๐งโุงูุง ุจูุช ุชุดุบูู ุงููุฏูู ู ุงูููุณููู ูู ุงูุฏุฑุฏุดุงุช ุงูุตูุชูู.

๐ฅโุงุณุชุทูุน ุงูุถุง ุงูุชุญูู ูู ุงูููุชููุจ ูุฏูู ุงู ุตูุช ุจุฌููุน ุงูุฏูู.

๐ฎโููุนุฑูู ููููู ุชุดุบููู ูู ูุฌููุนุชู ุงุถุบุท ุนูู ุฒุฑ ุงูุงูุฑ ุงูุจูุช ุจุงูุงุณูู ููู ุงุนุฑุถ ูู ุฌููุน ุงูุงูุงูุฑ.
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- ุงุถู ุงูุจูุช ููุฌููุนุชู .๏ธ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("- ุงูุงูุฑ ุชุดุบูู ุงูุจูุช .", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton(
                        "- ุงููุทูุฑ .", url=f"https://t.me/{OWNER_NAME}"),
                    InlineKeyboardButton(
                        "- ุฌุฑูุจ ุงูุฏุนู .", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ],
                [
                    InlineKeyboardButton(
                        "- ููุงู ุงูุณูุฑุณ .", url="https://t.me/UU_Le2"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- ููุงู ุงูุณูุฑุณ .", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "- ุฌุฑูุจ ุงูุฏุนู .", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**Hแดสสแด {message.from_user.mention()}, ษช'แด {BOT_NAME}**\n\nโจ Bแดแด ษชs แดกแดสแดษชษดษข ษดแดสแดแดสสส\n๐ Mส Mแดsแดแดส: [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\nโจ Bแดแด Vแดสsษชแดษด: `v{__version__}`\n๐ Pสสแดษขสแดแด Vแดสsษชแดษด: `{pyrover}`\nโจ Pสแดสแดษด Vแดสsษชแดษด: `{__python_version__}`\n๐ PสTษขCแดสสs แด?แดสsษชแดษด: `{pytover.__version__}`\nโจ Uแดแดษชแดแด Sแดแดแดแดs: `{uptime}`\n\n**Tสแดษดแดs าแดส Aแดแดษชษดษข แดแด สแดสแด, าแดส แดสแดสษชษดษข แด?ษชแดแดแด & แดแดsษชแด แดษด สแดแดส Gสแดแดแด's แด?ษชแดแดแด แดสแดแด** โค"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("๐ `PONG!!`\n" f"๐ป๏ธ `{delta_ping * 1000:.3f} ms`")
    
    
@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("**ษขแดแดแดษชษดษข สแดสแด แดแดษดแด**...")
    delta_ping = time() - start
    await m_reply.edit_text("๐ป **ุงุถููู ูู ูุฌููุนุชู**\n๐ป๏ธ **ูู ุจุฑูุนู ูุดุฑู ูู ุงููุฌููุนู**\n๐ป **ุงุฑุณู ุงูุฑ /join ูู ุงููุฌููุนู**\n๐ป **ูู ุจูุชุงุจู /play ูุงุณู ุงูุงุบููู ุงู /vplay  ูุงุณู ุงููุฏูู**\n๐ป ** ููุงู ุงูุจูุช** @UU_Le2**")


@Client.on_message(command(["uptime<", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "๐ค bot status:\n"
        f"โข **uptime:** `{uptime}`\n"
        f"โข **start time:** `{START_TIME_ISO}`"
    )
