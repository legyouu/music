# A Powerful Music Bot Property Of Muslim Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# @L120N 
# Owner LEGEND


from pyrogram import filters
from typing import List, Union
from config import COMMAND_PREFIXES


other_filters = filters.group & ~filters.edited & ~filters.via_bot & ~filters.forwarded
other_filters2 = (
    filters.private & ~filters.edited & ~filters.via_bot & ~filters.forwarded
)

# Roses are red, Violets are blue, A face like yours, Belongs in a zoo.

def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)