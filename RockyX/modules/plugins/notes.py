# Code Based by @RendyProjects

from RockyX import *
from RockyX.lib import *

from pykillerx.help import *

@M3_4_U(command(["notes"], cmd) & owner)
async def list_notes_command(client: Client, message: Message):
    await list_notes(client, message)

@M3_4_U(command(["delete"], cmd) & owner)
async def remove_notes_command(client: Client, message: Message):
    await remove_notes(client, message)

@M3_4_U(command(["save"], cmd) & owner)
async def save_notes_command(client: Client, message: Message):
    await save_note(client, message)

@M3_4_U(command(["get"], cmd) & owner)
async def get_notes_command(client: Client, message: Message):
    await call_notes(client, message)

add_command_help(
    "notes",
    [
        [f"save [name and reply to message]", "to save notes"],
        [f"get [name]", "to call notes"],
        [f"delete [name]", "to delete a note"],
        [f"notes", "to display a list of notes"],
    ],
)
