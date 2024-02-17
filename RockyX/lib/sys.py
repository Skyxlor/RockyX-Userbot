from RockyX import *
from RockyX.lib.cbn import make_carbon
from RockyX.lib.developer import shell_exec
import os
import asyncio

async def sysinfo(c, m):
    chat_id = m.chat.id
    install_system = os.system("apt-get install -y neofetch") if os else None
    if install_system:
         await install_system
    else:
         try:
             sysinfo = (await shell_exec("neofetch | sed 's/\x1B\\[[0-9;\\?]*[a-zA-Z]//g'"))[0]
             carbon = await make_carbon(sysinfo)
             await c.send_photo(chat_id, carbon, caption=f"Carbonised by {c.me.mention}")
         except Exception as e:
             await m.reply_text(str(e))
             return


async def send_photo_or_video(c, m):
    chat_id = m.chat.id
    link = (m.text.split(None, 1)[1] if len(m.command) != 1 else None or (m.reply_to_message.text if m.reply_to_message else None))
    link_new = m.reply_to_message.text if m.reply_to_message and "https://" in m.reply_to_message.text else None
    if not link:
        await m.reply_text("for example, this telegraph link can send mp4")
        return
    if link_new:
        send_other = c.send_video if link_new.endswith(".mp4") else c.send_photo
        links = link_new
    else:
        send_other = c.send_video if link.endswith(".mp4") else c.send_photo
        links = link
    try:
        await send_other(m.chat.id, links)
    except Exception as e:
        await m.reply_text(str(e))
