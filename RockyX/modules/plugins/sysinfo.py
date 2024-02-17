from RockyX import *
from RockyX.lib import *

@M3_4_U(command("sysinfo", cmd) & owner)
async def sysinfo_command(c: Client, m: Message):
    await sysinfo(c, m)


@M3_4_U(command("sendr", cmd) & owner)
async def send_other_link(c: Client, m: Message):
    await send_photo_or_video(c, m)
