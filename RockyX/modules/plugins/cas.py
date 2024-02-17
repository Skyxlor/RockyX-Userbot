from . import *
from RockyX.lib import *


@M3_4_U(command("cas", cmd) & owner)
async def cas_command(c: Client, m: Message):
    await cas_check(c, m)
