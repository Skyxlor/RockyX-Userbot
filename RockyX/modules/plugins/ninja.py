from RockyX import *
from RockyX.lib import *

@M3_4_U(command("facedetect2", cmd) & owner)
async def ninja_detect(client: Client, message: Message):
    await api_ninja_detect(client, message)

@M3_4_U(command(["dog", "dogs"], cmd) & owner)
async def ninja_dog_handler(client: Client, message: Message):
    await api_ninja_dogs(client, message)
