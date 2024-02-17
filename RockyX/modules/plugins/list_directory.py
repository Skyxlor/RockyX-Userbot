from . import *
from RockyX.lib import *

@M3_4_U(command("ls", cmd) & owner)
async def list_directories_cmd(c: Client, m: Message):
    await list_directories(c, m)
