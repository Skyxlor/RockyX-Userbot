from RockyX.lib import *

from pykillerx import *
from pykillerx.help import add_command_help

@M3_4_U(command(["speedtest"], cmd) & owner)
async def speed_test_command(client: Client, message: Message):
    await speed_test(client, message)

@M3_4_U(command("kping", cmd) & owner)
async def kping_command(client: Client, message: Message):
    await kping(client, message)

@M3_4_U(command("ping", cmd) & owner)
async def ping_command(client: Client, message: Message):
    await ping(client, message)

@M3_4_U(command(["fck"], cmd) & owner)
async def fuck_command(client: Client, message: Message):
    await ping_fuck(client, message)


add_command_help(
    "ping",
    [
        [f"ping or .kping", "Check bot alive or not."],
        ["fck", "Check fucking."],
    ],
)
