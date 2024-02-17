from RockyX import *
from RockyX.lib import *

@M3_4_U(command("fbdl", cmd) & owner)
async def facebook_handler(client: Client, message: Message):
    await facebook_downloader(client, message)
