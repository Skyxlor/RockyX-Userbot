from RockyX import *
from RockyX.lib import *

from pykillerx.help import *

@M3_4_U(command("rmbg", cmd) & owner)
async def rmbg_command(c: Client, m: Message):
    await rmbg_background(c, m)
