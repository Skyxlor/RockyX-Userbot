from RockyX import *
from RockyX.lib import *

from pykillerx.help import *

@M3_4_U(command(["limit", "limited"], cmd) & owner)
async def spamban_command(client: Client, m: Message):
    await spamban(client, m)

add_command_help(
    "limited",
    [
        [f"limit or .limited", "Check Limit telegram from @SpamBot."],
    ],
)
