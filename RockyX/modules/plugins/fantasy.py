from RockyX import *
from RockyX.lib import *

from pykillerx.help import *

@M3_4_U(command(["fantasy"], cmd) & owner)
async def fantasy_handler(client: Client, message: Message):
    await fantasy_portrait(client, message)
