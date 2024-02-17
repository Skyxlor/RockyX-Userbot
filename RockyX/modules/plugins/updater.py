from RockyX import *
from RockyX.lib import *

@M3_4_U(command("update", cmd) & owner)
async def update_handler_fixed(client: Client, message: Message):
    await upstream(client, message)

@M3_4_U(command("goupdate", cmd) & owner)
async def update_handler(client: Client, message: Message):
    await updatees(client, message)
