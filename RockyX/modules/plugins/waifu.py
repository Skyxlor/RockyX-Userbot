from RockyX import *
from RockyX.lib import *

@M3_4_U(command("waifu", cmd) & owner)
async def waifu_hanlder(client: Client, message: Message):
    await api_waifu_main(client, message)
