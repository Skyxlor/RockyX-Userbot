from RockyX import *
from RockyX.lib import *

@M3_4_U(command("listgrup", cmd) & owner)
async def list_member_hndlr(client: Client, message: Message):
    await list_show_grup(client, message)

@M3_4_U(command("listdev", cmd) & owner)
async def list_devs_hndlr(client: Client, message: Message):
    await list_show_dev(client, message)
