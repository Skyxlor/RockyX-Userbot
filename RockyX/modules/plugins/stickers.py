from RockyX import *
from RockyX.lib import *

from pykillerx.help import *

@M3_4_U(command(["tikel", "kang", "steal"], cmd) & owner)
async def kang_command(client: Client, message: Message):
    await kang(client, message)

@M3_4_U(command(["packinfo", "stickerinfo"], cmd) & owner)
async def packinfo_command(client: Client, message: Message):
    await packinfo(client, message)

@M3_4_U(command(["sticker", "stickers"], cmd) & owner)
async def cb_sticker_command(client: Client, message: Message):
    await cb_sticker(client, message)

@M3_4_U(command("tiny", cmd) & owner)
async def tinying_command(client: Client, message: Message):
    await tinying(client, message)

@M3_4_U(command(["mmf", "memify"], cmd) & owner)
async def memify_command(client: Client, message: Message):
    await memify(client, message)

add_command_help(
    "sticker",
    [
        [f"kang `reply` image", "Reply .kang To Sticker Or Image To Add To Sticker Pack."],
        [f"kang [emoji] `or` .double [emoji]", "To add and custom emoji stickers to your sticker pack."],
        [f"packinfo `or` .stickerinfo", "To Get Sticker Pack Information."],
        [f"mtoi [reply ke sticker] or .getsticker [reply ke sticker]", "Reply to sticker to get sticker photo."],
        ["stickers [nama sticker]", "To find sticker packs."],
    ],
)


add_command_help(
    "memify",
    [
        [f"mmf Top Text ; Bottom Text", "Reply To Message Sticker or Photo will be Converted to the specified meme text sticker."],
    ],
)


add_command_help(
    "tiny",
    [
        [f"tiny [reply ke photo/sticker]", "To Change the Sticker to be Small."],
    ],
)


