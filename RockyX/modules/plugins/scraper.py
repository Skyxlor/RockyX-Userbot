from RockyX import *
from RockyX.lib import *

from pykillerx.help import *

@M3_4_U(command(["invite"], cmd) & owner)
async def invite_command(client: Client, message: Message):
    await invite_user(client, message)

@M3_4_U(command(["inviteall"], cmd) & owner)
async def inv(client: Client, message: Message):
    await invite_all(client, message)

@M3_4_U(command("invitelink", cmd) & owner)
async def invite_link_ok(client: Client, message: Message):
    await invite_link(client, message)

add_command_help(
    "scraper",
    [
        ["invitelink", "Get your private invite link. [Need Admin]"],
        ["invite @username", "to invite someone."],
        ["inviteall @username", "Mass adding (can affect your account)."],
    ],
)
