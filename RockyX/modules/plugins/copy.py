# Copyright (C) 2020-2023 Skyxlor <https://github.com/Skyxlor>
#
# This file is part of Skyxlor project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# Credits by : https://t.me/M3_4_U
# Don't remove credits

from RockyX import *
from RockyX.lib import *

from pykillerx.help import *

@M3_4_U(command("copy", cmd) & owner)
async def nothing(client: Client, message: Message):
    await copy_message(client, message)

@M3_4_U(command("take", cmd) & owner)
async def lmao_this(client: Client, message: Message):
    await take_corret(client, message)

add_command_help(
    "copy",
    [
        [f"copy [link]", "to copy link of public channel"],
    ],
)
