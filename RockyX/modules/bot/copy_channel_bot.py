# Copyright (C) 2020-2023 Skyxlor <https://github.com/Skyxlor>
#
# This file is part of Skyxlor project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# Credits by : https://t.me/M3_4_U

from RockyX import app
from RockyX.lib import *

@app.on_message(filters.private)
async def take_channel(client: Client, message: Message):
    await ass_copy_link(client, message)
