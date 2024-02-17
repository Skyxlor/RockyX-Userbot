from RockyX import *
from RockyX.lib import *

from pykillerx.help import *

@M3_4_U(command(["vid", "video"], cmd) & owner)
async def yt_video_command(c: Client, m: Message):
    await yt_video(c, m)

@M3_4_U(command("ytv", cmd) & owner)
async def ytv_dl_command(c: Client, m: Message):
    await ytv_dl(c, m)

@M3_4_U(command("yta", cmd) & owner)
async def yta_dl_command(c: Client, m: Message):
    await yta_dl(c, m)

@M3_4_U(command("ytp", cmd) & owner)
async def ytp_dl_command(c: Client, m: Message):
    await ytp_dl(c, m)

add_command_help(
    "youtube",
    [
        [f"ytv <link>", "Download Video from YouTube and then upload it to telegram.."],
        [f"yta <link>", "Download Audio from YouTube and then upload it to telegram.."],
        [f"ytp <link>", "Download Playlist from YouTube.."],
        [f"video <query>", "Download Video from YouTube and then upload it to telegram."],
    ],
)
