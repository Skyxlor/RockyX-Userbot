from pyrogram import *
from pyrogram.types import *

from RockyX.lib import *
from RockyX import *

@app.on_inline_query()
@inline_wrapper
async def inline_query_handler_ok(client: Client, query):
    await inline_query_handler(client, query)
