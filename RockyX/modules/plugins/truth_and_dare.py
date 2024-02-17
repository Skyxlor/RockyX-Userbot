from RockyX import *
from RockyX.lib.slp import truth_string_str, dare_string_str_2
from RockyX.lib import *

@M3_4_U(command("truth", cmd) & owner)
async def truth_command(c: Client, m: Message):
    await truth_string_str(c, m)

@M3_4_U(command("dare", cmd) & owner)
async def dare_command(c: Client, m: Message):
    await dare_string_str_2(c, m)

