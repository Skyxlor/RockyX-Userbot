from RockyX import *
from RockyX.lib import *

@M3_4_U(command("tagpremium", cmd) & owner)
async def user_premium_fixed(c: Client, m: Message):
    await user_premium(c, m)
