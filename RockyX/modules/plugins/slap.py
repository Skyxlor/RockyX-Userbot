from RockyX import *
from RockyX.lib.slp import slap_template_fixed, slap_funny_lol_fixed
from RockyX.lib import *

@M3_4_U(command("slap", cmd) & owner)
async def slap_english_command(c: Client, m: Message):
    await slap_template_fixed(c, m)


@M3_4_U(command("slape", cmd) & owner)
async def slap_english_command_2(c: Client, m: Message):
    await slap_funny_lol_fixed(c, m)
