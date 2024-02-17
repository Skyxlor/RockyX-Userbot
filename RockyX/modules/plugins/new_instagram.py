from RockyX import *
from RockyX.lib import *

@M3_4_U(command("igdl", cmd) & owner)
async def instagram_handler(client: Client, message: Message):
    await instagram_downloader(client, message)
