# A Powerful Music Bot Property Of Muslim Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# @L120N 
# Owner LEGEND

from typing import List
from pyrogram.types import Chat
from cache.admins import get as gett, set

async def get_administrators(chat: Chat) -> List[int]:
    get = gett(chat.id)

    if get:
        return get
    else:
        administrators = await chat.get_members(filter="administrators")
        to_set = []

        for administrator in administrators:
            if administrator.can_manage_voice_chats:
                to_set.append(administrator.user.id)

        set(chat.id, to_set)
        return await get_administrators(chat)

                
# Roses are red, Violets are blue, A face like yours, Belongs in a zoo.