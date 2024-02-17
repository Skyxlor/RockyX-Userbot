from RockyX import *
from RockyX.lib import *

from pykillerx.help import *

@M3_4_U(command("carbon", cmd) & owner)
async def carbon_func_command(client: Client, message: Message):
    await carbon_func(client, message)
