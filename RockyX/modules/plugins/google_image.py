from RockyX import *
from RockyX.lib import *

from pykillerx.help import *

@M3_4_U(command("img", cmd) & owner)
async def generate_image_command(c: Client, m: Message):
    await generate_image(c, m)
