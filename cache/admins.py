# A Powerful Music Bot Property Of Muslim Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# @L120N 
# Owner LEGEND



from config import admins
from typing import Dict, List


admins: Dict[int, List[int]] = {}


def set(chat_id: int, admins_: List[int]):
    admins[chat_id] = admins_


def get(chat_id: int) -> List[int]:
    if chat_id in admins:
        return admins[chat_id]
    return []

# Roses are red, Violets are blue, A face like yours, Belongs in a zoo.