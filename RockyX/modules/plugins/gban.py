from RockyX import *
from RockyX.lib import *

from pykillerx.blacklist import *
from pykillerx.help import *

# Code Credits by: @mrismanaziz

@M3_4_U(command("cgban", cmd) & filters.user(DEVS) & ~owner)
@M3_4_U(command("gban", cmd) & filters.me)
async def gban_user_command(client: Client, message: Message):
    await gban_user_all(client, message)

@M3_4_U(command("cungban", cmd) & filters.user(DEVS) & ~owner)
@M3_4_U(command("ungban", cmd) & filters.me)
async def ungban_user_command(client: Client, message: Message):
    await ungban_user_all(client, message)

@M3_4_U(command("listgban", cmd) & owner)
async def gbanlist_command(client: Client, message: Message):
    await gbanlist_all(client, message)

@M3_4_U(command("gmute", cmd) & owner)
async def gmute_user_command(client: Client, message: Message):
    await gmute_user_all(client, message)

@M3_4_U(command("ungmute", cmd) & owner)
async def ungmute_user_command(client: Client, message: Message):
    await ungmute_user_all(client, message)

@M3_4_U(command("listgmute", cmd) & owner)
async def gmutelist_command(client: Client, message: Message):
    await gmutelist_all(client, message)

@M3_4_U(filters.incoming & filters.group)
async def globals_check(client: Client, message: Message):
    await globals_check_all(client, message)

add_command_help(
    "globals",
    [
        [f"gban <reply/username/userid>", "do global banned to all groups where you as admin."],
        [f"ungban <reply/username/userid>", "cancel global banned."],
        ["listgban", "displays the global banned list."],
    ],
)
