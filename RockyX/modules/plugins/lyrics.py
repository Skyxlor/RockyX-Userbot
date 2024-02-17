from RockyX import *
from RockyX.lib import *

@M3_4_U(command("lyrics", cmd) & owner)
async def lyrics_command(client: Client, message: Message):
    await lyrics(client, message)
