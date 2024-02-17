from RockyX import *
from RockyX.lib import *

from pykillerx.help import *

@M3_4_U(command("santet", cmd) & owner)
async def santet_lu_fix(client: Client, message: Message):
    await typewriter(client, message)

@M3_4_U(command("whatsapp", cmd) & owner)
async def wa_lu_fix(client: Client, message: Message):
    await whatsapp_hack(client, message)

@M3_4_U(command("macos", cmd) & owner)
async def macos_lu_fix(client: Client, message: Message):
    await macos_animation(client, message)

@M3_4_U(command("police", cmd) & owner)
async def police_lu_fix(client: Client, message: Message):
    await police_animation(client, message)

@M3_4_U(command("linux", cmd) & owner)
async def linux_lu_fix(client: Client, message: Message):
    await linux_hacker(client, message)

@M3_4_U(command("hack", cmd) & owner)
async def hacker_lu_fix(client: Client, message: Message):
    await hacker_user(client, message)

@M3_4_U(command(["kontol", "dick"], cmd) & owner)
async def kontol_lu_fix(client: Client, message: Message):
    await penis_tolol(client, message)

@M3_4_U(command(["bye"], cmd) & owner)
async def leave_lu_fix(client: Client, message: Message):
    await bye_prank(client, message)

@M3_4_U(command(["suicide"], cmd) & owner)
async def bundir_lu_fix(client: Client, message: Message):
    await bundir_ghosting(client, message)

@M3_4_U(command(["snake"], cmd) & owner)
async def ular_lu_fix(client: Client, message: Message):
    await ular_kaget(client, message)

@M3_4_U(command(["y"], cmd) & owner)
async def jembol_lu_fix(client: Client, message: Message):
    await jembol_like(client, message)

@M3_4_U(command(["cinta"], cmd) & owner)
async def cinta_lu_fix(client: Client, message: Message):
    await cinta_goblok(client, message)

add_command_help(
    "animation",
    [
        ["santet", "usage: "],
        ["whatsapp", "usage: "],
        ["macos", "usage: "],
        ["police", "usage: "],
        ["linux", "usage: "],
        ["hack", "usage: "],
        [f"kontol or .dick ", "usage: "],
        ["bye", "usage: prank left"],
        ["suicide", "usage: "],
        ["snake", "usage: "],
        ["y", "usage: like"],
        ["cinta", "usage: "],
    ],
)
