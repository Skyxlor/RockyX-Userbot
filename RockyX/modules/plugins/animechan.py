from RockyX import *
from RockyX.lib import *

@M3_4_U(command("animequote", cmd) & owner)
async def animechan_hanlder(client: Client, message: Message):
    await api_animechan_new(client, message)
