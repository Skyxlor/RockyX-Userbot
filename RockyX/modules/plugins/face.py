from RockyX import *
from RockyX.lib import *

from pykillerx.help import *

@M3_4_U(command(["toonify", "cartoon"], cmd) & owner)
async def toonify_handler(c: Client, m: Message):
    await toonify(c, m)

add_command_help(
    "deepai",
    [
        [f"cartoon or .toonify [reply to image]", "to cartoon image using the deepai api."],
    ],
)
