from RockyX import *
from RockyX.lib import *

from pykillerx.help import *

@M3_4_U(command(["tr", "translate"], cmd) & owner)
async def pytrans_tr_command(_, message: Message):
    await pytrans_tr(_, message)
