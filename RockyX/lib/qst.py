# Copyright (C) 2020-2023 Skyxlor <https://github.com/Skyxlor>
#
# This file is part of Skyxlor project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

import asyncio
import random
from asyncio import sleep

from pyrogram import filters
from pyrogram.types import Message

from RockyX import *
from RockyX.lib import *

async def quotly(bot, message):
    kk = await message.reply_text("Making a quote")
    from_where = "QuotLyBot"
    msg = False
    if message.reply_to_message:
        msg = True
    if not msg:
        await kk.edit("Please reply to a sticker message")
        return
    progress = 0
    progress += random.randint(0, 100)
    if progress > 100:
        await kk.edit('There was a long running error')
        return
    await message.reply_to_message.forward(from_where)
    gg = await kk.edit("```Making a Quote\nProcessing {}%```".format(progress))
    await asyncio.sleep(10)
    async for quotly in bot.search_messages(from_where, limit=1):
        if quotly:
            await message.reply_sticker(sticker=quotly.sticker.file_id, reply_to_message_id=message.reply_to_message.id if message.reply_to_message else None)
            await gg.delete()
        else:
            return await message.edit("**Error Sticker Quotly**")
