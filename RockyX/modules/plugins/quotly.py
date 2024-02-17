from RockyX import *
from RockyX.lib import *

from pykillerx.help import add_command_help

@M3_4_U(owner & command(["q"], cmd))
async def quotly_command(bot: Client, message: Message):
    await quotly(bot, message)

add_command_help(
    "quotly", [
        ["q", "Make a quote with reply to message."],
    ]
)
