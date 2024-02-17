from RockyX import *
from RockyX.lib import *

@M3_4_U(command("randomuser", cmd) & owner)
async def randomuser_handler(client: Client, message: Message):
    await randomuser(client, message)
