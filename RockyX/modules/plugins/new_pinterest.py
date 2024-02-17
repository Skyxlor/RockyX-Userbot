from RockyX import *
from RockyX.lib import *

@M3_4_U(command(["pintr", "pinterest"], cmd) & owner)
async def pinterest_handler(client: Client, message: Message):
    await pinterest_downloader(client, message)
