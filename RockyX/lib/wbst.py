import asyncio
from pyrogram.types import *
from pyrogram import *
from pyrogram import Client as ren
from pyrogram import Client

from RockyX import *
from RockyX.lib import *

from pykillerx import *
from pykillerx.helper.basic import *
from pykillerx.helper.hacking import *
from pykillerx.helper import *

async def webshot(client, message):
    ren = await edit_or_reply(message, "`Processing...`")
    try:
        user_link = message.command[1]
        try:
            full_link = f"https://webshot.deam.io/{user_link}/?width=1920&height=1080?delay=2000?type=png"
            await client.send_photo(
                message.chat.id,
                full_link,
                caption=f"**Screenshot of the page ⟶** {user_link}",
            )
        except Exception as dontload:
            await message.edit(f"Error! {dontload}\nTrying again create screenshot...")
            full_link = f"https://mini.s-shot.ru/1920x1080/JPEG/1024/Z100/?{user_link}"
            await client.send_photo(
                message.chat.id,
                full_link,
                caption=f"**Screenshot of the page ⟶** {user_link}",
            )
        await ren.delete()
    except Exception as error:
        await ren.delete()
        await client.send_message(
            message.chat.id, f"**Something went wrong\nLog:{error}...**"
        )
