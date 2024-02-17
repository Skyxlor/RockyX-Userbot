from RockyX import *
from RockyX.lib import *

from pykillerx.help import add_command_help

@M3_4_U(command(["webshot", "ss"], cmd) & owner)
async def webshot_command(client: Client, message: Message):
    await webshot(client, message)

add_command_help(
    "webshot",
    [
        [f"webshot <link> or .ss <link>", "to screenshot the given web page"],
    ],
)
