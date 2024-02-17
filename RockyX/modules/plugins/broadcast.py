from RockyX import *
from RockyX.lib import *

from pykillerx.help import *

@M3_4_U(command(["gcast"], cmd) & owner)
async def gcast_command(client: Client, message: Message):
    await gcast_all(client, message)

@M3_4_U(command(["gforward"], cmd) & owner)
async def gforward_command(client: Client, message: Message):
    await gforward_all(client, message)

@M3_4_U(command(["guforward"], cmd) & owner)
async def guforward_command(client: Client, message: Message):
    await guforward_all(client, message)

@M3_4_U(command(["gucast"], cmd) & owner)
async def gucast_command(client: Client, message: Message):
    await gucast_all(client, message)

add_command_help(
    "broadcast",
    [
        [f"gcast [text/reply]", "Sending Global Broadcast messages to all groups you are logged into. (Can Send Media/Sticker)"],
        [f"gforward [reply]", "Sending Global Broadcast message to all group forwarded messages"],
        [f"guforward [reply]", "Sending Global Broadcast messages to all incoming Private Massages Forward"],
        [f"gucast [text/reply]", "Sending Global Broadcast messages to all incoming Private Massages / PCs. (Can Send Media/Sticker)"],
    ],
)
