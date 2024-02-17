from RockyX import *
from RockyX.lib import *


@M3_4_U(command("logo", cmd) & owner)
async def logo_command(client: Client, message: Message):
    await logo_write(client, message)
