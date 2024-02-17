from RockyX import *
from RockyX.lib import *

from pykillerx.help import *

@M3_4_U(command(["help", "helpme"], cmd) & owner)
async def module_help_cmd(client: Client, message: Message):
    await module_help(client, message)

@M3_4_U(command(["plugins"], cmd) & owner)
async def module_helper_cmd(client: Client, message: Message):
    await module_helper(client, message)
