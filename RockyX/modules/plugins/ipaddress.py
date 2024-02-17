from RockyX import *
from RockyX.lib import *

@M3_4_U(command("ip", cmd) & owner)
async def location_hanlder(client: Client, message: Message):
    await hacker_lacak_target(client, message)

@M3_4_U(command("ipd", cmd) & owner)
async def domain_hanlder(client: Client, message: Message):
    await whois_domain_target(client, message)
