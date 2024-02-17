from RockyX import *
from RockyX.lib import *

from pykillerx.help import add_command_help

@M3_4_U(command(["unblock"], cmd) & owner)
async def unblock_user_func(client: Client, message: Message):
    await unblock_user(client, message)

@M3_4_U(command(["block"], cmd) & owner)
async def block_user_func(client: Client, message: Message):
    await block_user(client, message)

@M3_4_U(command(["setname"], cmd) & owner)
async def setname_command(client: Client, message: Message):
    await setname(client, message)

@M3_4_U(command(["setbio"], cmd) & owner)
async def set_bio_command(client: Client, message: Message):
    await set_bio(client, message)

@M3_4_U(command(["setpfp"], cmd) & owner)
async def set_pfp_command(client: Client, message: Message):
    await set_pfp(client, message)

add_command_help(
    "profile",
    [
        ["block", "to block someone on telegram"],
        ["unblock", "to unblock someone on telegram"],
        ["setname", "set your profile name."],
        ["setbio", "set an bio."],
        ["setpfp", f"reply with image to set your profile pic."],
    ],
)
