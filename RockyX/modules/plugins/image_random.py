from RockyX import *
from RockyX.lib import *

from pykillerx.help import add_command_help

@M3_4_U(command("cat", cmd) & owner)
async def cat_image_fixed(client: Client, message: Message):
    await api_big_cat(client, message)

@M3_4_U(command("dog2", cmd) & owner)
async def image_fixed(client: Client, message: Message):
    await api_ceo_dog(client, message)

@M3_4_U(command("dog3", cmd) & owner)
async def image_fixed_2(client: Client, message: Message):
    await api_ceo_dog2(client, message)

@M3_4_U(command("fox", cmd) & owner)
async def image_fixed_3(client: Client, message: Message):
    await api_fox_ca(client, message)

@M3_4_U(command("fox", cmd) & owner)
async def image_fixed_3(client: Client, message: Message):
    await api_fox_ca(client, message)

@M3_4_U(command("frybot", cmd) & owner)
async def frybot_handler(client: Client, message: Message):
    await frybot(client, message)

@M3_4_U(command("quotes", cmd) & owner)
async def quotes_handler(client: Client, message: Message):
    await api_quotes_new(client, message)

@M3_4_U(command("findmovie", cmd) & owner)
async def movie_handler(client: Client, message: Message):
    await api_movie_info(client, message)
    

add_command_help(
    "apitools",
    [
        ["cat", "to using api cat."],
        ["dog2", "to using api dog."],
        ["dog3", "to using api dog versi 2."],
        ["fox", "to using api fox ."],
        ["waifu", "to using api anime waifu."],
        ["animequote", "to using api animechan."],
        ["ip", "to using api get trace ip address."],
        ["randomuser", "to using api random user."],
        ["quotes", "to using api quotes"],
        ["findmovie", "to using api IMDB"],

    ],
)
