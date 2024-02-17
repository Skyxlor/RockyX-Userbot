from RockyX import *
from RockyX.lib import *

from pykillerx.help import add_command_help

@M3_4_U(command(["pat", "pats"], cmd) & owner)
async def pat_handler(c: Client, m: Message):
    await give_pats(c, m)

add_command_help(
    "pats",
    [
        [".pat | .pats", "Give pats."],
    ],
)
