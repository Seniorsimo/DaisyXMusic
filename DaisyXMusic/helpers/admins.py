from typing import List

from pyrogram import enums
from pyrogram.types import Chat

from DaisyXMusic.function.admins import get as gett
from DaisyXMusic.function.admins import set


async def get_administrators(chat: Chat) -> List[int]:
    get = gett(chat.id)

    if get:
        return get
    else:
        administrators = chat.get_members(filter=enums.ChatMembersFilter.ADMINISTRATORS)
        to_set = []

        async for administrator in administrators:
            if administrator.can_manage_voice_chats:
                to_set.append(administrator.user.id)

        set(chat.id, to_set)
        return await get_administrators(chat)
