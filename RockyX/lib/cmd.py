# Created By @M3_4_U

from pyrogram import *
from pyrogram import Client as ren
from pyrogram.types import *
import os 
from os import getenv
from RockyX import PREFIXES

handler = [".", "^"]

cmd = handler

if handler:
    cmd = ["!", "+"]
elif PREFIXES:
    cmd = PREFIXES
else:
    cmd = None

command = filters.command
regex = filters.regex 
owner = filters.me
private = filters.private
M3_4_U = ren.on_message
M3_4_U_edited = ren.on_edited_message
