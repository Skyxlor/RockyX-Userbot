from RockyX import *
from RockyX.lib import *

from pykillerx.help import *

@M3_4_U(((filters.group & filters.mentioned) | private) & ~owner & ~filters.service, group=3)
async def collect_afk_mentioned(bot: Client, message: Message):
    await collect_afk_messages(bot, message)

@M3_4_U(command("afk", cmd) & owner, group=3)
async def afk_set_cmd(bot: Client, message: Message):
    await afk_set_all(bot, message)

@M3_4_U(command("afk", cmd) & owner, group=3)
async def afk_unset_cmd(bot: Client, message: Message):
    await afk_unset_all(bot, message)

if AFK:
   @M3_4_U(owner, group=3)
   async def auto_afk_unset_cmd(bot: Client, message: Message):
       await auto_afk_unset_all(bot, message)

add_command_help(
    "afk",
    [
        ["afk", "Activates AFK mode with reason as anything after .afk\nUsage: ```.afk <reason>```"],
        ["afk", "Deactivates AFK mode."],
    ],
)
