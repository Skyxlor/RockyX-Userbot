from RockyX import *
from RockyX.lib import *

from pykillerx.help import add_command_help

@M3_4_U(command("war", cmd) & owner)
async def war_goblok(client: Client, message: Message):
    await toxic_fixed1(client, message)

@M3_4_U(command("dih", cmd) & owner)
async def dih_goblok(client: Client, message: Message):
    await toxic_fixed2(client, message)

@M3_4_U(command("gembel", cmd) & owner)
async def gembel_goblok(client: Client, message: Message):
    await toxic_fixed3(client, message)

@M3_4_U(command("sokab", cmd) & owner)
async def sokap_goblok(client: Client, message: Message):
    await toxic_fixed4(client, message)

@M3_4_U(command("ded", cmd) & owner)
async def ded_goblok(client: Client, message: Message):
    await toxic_fixed5(client, message)

@M3_4_U(command("caper", cmd) & owner)
async def caper_goblok(client: Client, message: Message):
    await toxic_fixed6(client, message)

@M3_4_U(command("lo", cmd) & owner)
async def lo_goblok(client: Client, message: Message):
    await toxic_fixed7(client, message)

@M3_4_U(command("woi", cmd) & owner)
async def woi_goblok(client: Client, message: Message):
    await toxic_fixed8(client, message)

@M3_4_U(command("ngatur", cmd) & owner)
async def ngatur_goblok(client: Client, message: Message):
    await toxic_fixed9(client, message)

@M3_4_U(command("ubot", cmd) & owner)
async def ubot_goblok(client: Client, message: Message):
    await toxic_fixed10(client, message)

@M3_4_U(command("d", cmd) & owner)
async def d_goblok(client: Client, message: Message):
    await toxic_fixed11(client, message)

@M3_4_U(command("e", cmd) & owner)
async def e_goblok(client: Client, message: Message):
    await toxic_fixed12(client, message)

@M3_4_U(command("f", cmd) & owner)
async def f_goblok(client: Client, message: Message):
    await toxic_fixed13(client, message)

@M3_4_U(command("i", cmd) & owner)
async def i_goblok(client: Client, message: Message):
    await toxic_fixed14(client, message)

@M3_4_U(command("qi", cmd) & owner)
async def q_goblok(client: Client, message: Message):
    await toxic_fixed15(client, message)

@M3_4_U(command("t", cmd) & owner)
async def t_goblok(client: Client, message: Message):
    await toxic_fixed16(client, message)

@M3_4_U(command("u", cmd) & owner)
async def u_goblok(client: Client, message: Message):
    await toxic_fixed17(client, message)

add_command_help(
    "toxic",
    [
        ["war", "usage: "],
        ["dih", "usage: "],
        ["gembel", "usage: "],
        ["sokab", "usage: "],
        ["ded", "usage: "],
        ["caper", "usage: "],
        ["lo", "usage: "],
        ["woi", "usage: "],
        ["ngatur", "usage: "],
        ["ubot", "usage: "],
        ["d", "usage: "],
        ["e", "usage: "],
        ["f", "usage: "],
        ["i", "usage: "],
        ["qi", "usage: "],
        ["t", "usage: "],
        ["u", "usage: "],

    ],  
)

