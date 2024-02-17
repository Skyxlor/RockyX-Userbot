# this upload file 

import asyncio
import humanize
from pyrogram import Client, filters
from pyrogram.types import Message

from RockyX import *
from RockyX.lib import *

async def progress_callback(current, total, bot: Client, message: Message):
    if int((current / total) * 100) % 25 == 0:
        await message.edit(f"{humanize.naturalsize(current)} / {humanize.naturalsize(total)}")


async def upload_helper(bot, message):
    if len(message.command) > 1:
        await bot.send_document(message.chat.id, message.command[1], progress=progress_callback, progress_args=(bot, message))
    else:
        await message.edit('No path provided.')
