# A Powerful Music Bot Property Of Muslim Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# @L120N 
# Owner LEGEND


from config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME
from pyrogram import Client
from pytgcalls import PyTgCalls

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "asadmodules"},
)

user = Client(
    SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
)

call_py = PyTgCalls(user)


# Roses are red, Violets are blue, A face like yours, Belongs in a zoo.