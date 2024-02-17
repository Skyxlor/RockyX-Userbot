from RockyX import *
from RockyX.lib import *

from pykillerx.help import *

@M3_4_U(command(["tg", "telegraph"], cmd) & owner)
async def telegraph_command(client: Client, message: Message):
    await telegraph_upload(client, message)

add_command_help(
    "telegraph",
    [
        [f"telegraph or .tg", "Reply to messages or media to upload them to the telegraph."],
    ],
)
