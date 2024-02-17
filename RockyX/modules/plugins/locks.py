from RockyX import *
from RockyX.lib import *

from pykillerx.help import *

@M3_4_U(command(["lock", "unlock"], cmd) & owner)
async def locks_cmd(client: Client, message: Message):
    await locks_all_or_unlock_all(client, message)

@M3_4_U(command("locks", cmd) & owner)
async def locktypes_cmd(client: Client, message: Message):
    await locktypes(client, message)

add_command_help(
    "locks",
    [
        ["lock [all or specific]", "restrict user to send."],
        [
            "unlock [all or specific]",
            "Unrestrict\n\nSupported Locks / Unlocks:` `msg` | `media` | `stickers` | `polls` | `info`  | `invite` | `webprev` |`pin` | `all`.",
        ],
    ],
)
