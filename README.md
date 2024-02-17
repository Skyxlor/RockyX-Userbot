![20230312_175518](https://telegra.ph/file/d3f3449f95b5f6088fe13.jpg)

<h2 align="center"> 🐯 RockyX-Userbot 🐯</h2> 

![Repo Size](https://img.shields.io/github/repo-size/Skyxlor/RockyX-Userbot)
![License](https://img.shields.io/github/license/Skyxlor/RockyX-Userbot)
![Python Version](https://img.shields.io/badge/python-3.x.x-aqua)
![Maintained](https://img.shields.io/badge/Maintained%20%3F-Yes-orange)
![Files](https://img.shields.io/github/directory-file-count/Skyxlor/RockyX-Userbot?label=repo%20files)


## 📝 Disclaimer 📝
```
️                       ⚠️ WARNING FOR YOU ️ ️⚠️
   RockyX is used to help your account activities on Telegram
   We are not responsible for what you misuse in this repository
   !  Be careful when using this repository!
   If one of the members misuses this repository, we are forced to ban you
   Never ever abuse this repository
```

## 🛠️ VPS 🛠️
```console
Rendy@Ubuntu~ $ sudo apt update && sudo apt upgrade -y
Rendy@Ubuntu~ $ git clone https://github.com/Skyxlor/RockyX-Userbot && cd RockyX-Userbot
Rendy@Ubuntu~ $ bash install.sh
Rendy@Ubuntu~ $ pip3 install -r req *
Rendy@Ubuntu~ $ cp config.ini_sample config.ini
Rendy@Ubuntu~ $ nano config.ini
Rendy@Ubuntu~ $ screen -S tiger
Rendy@Ubuntu~ $ python3 -m RockyX
# ctrl a + d 
```

## 💎 Example Plugins 💎
* this module plugins : [Click Here](https://github.com/Skyxlor/RockyX-Userbot/tree/dev/RockyX/modules/plugins)

```python
from RockyX import *
from RockyX.lib import * 

from pykillerx.help import add_command_help 

@M3_4_U(command("example", cmd) & owner)
async def hello_world_command(client: Client, message: Message):
    await hello_world(client, message)
```


* this module lib : [Click Here](https://github.com/Skyxlor/RockyX-Userbot/tree/dev/RockyX/lib)
* you can add <code>__init__.py</code>
* don't forget to add files `example.py`
* like example : `from .example import *`

```python
# your own : @example or https://t.me/M3_4_U

async def hello_world(client, message):
    await client.send_message(message.chat.id, "Hello World")
```
* Code : [pull requests](https://github.com/Skyxlor/RockyX-Userbot/pulls)

## Example Api Tools

* [x] <b>this is available api</b> : [`https://www.jsonapi.co/public-api`](https://www.jsonapi.co/public-api)
* [x] <b>tiktok no watermark</b> : [`https://rapidapi.com/yi005/api/tiktok-video-no-watermark2/`](https://rapidapi.com/yi005/api/tiktok-video-no-watermark2/)
* [x] <b>facebook downloader</b> : [`https://rapidapi.com/officialofun-C-wpfpix418/api/facebook-video-and-reel-downloader`](https://rapidapi.com/officialofun-C-wpfpix418/api/facebook-video-and-reel-downloader)
* [x] <b>openai chatgpt</b> : [`https://rapidapi.com/openai-api-openai-api-default/api/openai80`](https://rapidapi.com/openai-api-openai-api-default/api/openai80)

* <b>sure make plugins example</b> `api_example.py`
```python
import requests

API_URL_EXAMPLE = "your api here"
response = requests.get(API_URL_EXAMPLE)
if response.status_code == 200:
    data_example = response.json()
    try:
        url_image = data_example["check_example_json"]
    except Exception as e: # or KeyError
        # using await or print()
        return 
    if url_image:
         # your own code 
    else:
         # your own code 
else:
    # something 
```

## Example Python File Open
```python 

import requests
import os

url = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fwallpapers.com%2Fimages%2Fhd%2Frandom-objects-alt-aesthetic-2zgd29x0bplv01u5.jpg&tbnid=1RO38bzjeP2n_M&vet=1&imgrefurl=https%3A%2F%2Fwallpapers.com%2Fwallpapers%2Frandom-objects-alt-aesthetic-2zgd29x0bplv01u5.html&docid=woUVzf9ut-iezM&w=1080&h=1920&hl=id&source=sh%2Fx%2Fim"
download = requests.get(url)
send_image_url = "example.jpg"
with open(send_image_url, "wb") as f:
    f.write(download.content)
await client.send_photo(message.chat.id, photo=send_image_url)
os.remove(send_image_url)
```

### Obtaining `sp_dc` and `sp_key` cookies

Spotcast uses two cookies to authenticate against Spotify in order to have access to the required services.

To obtain the cookies these different methods can be used:

#### Chrome based browser

##### Chrome web console

1. Open a new __Incognito window__ at [`https://open.spotify.com`](https://open.spotify.com) and login to Spotify.
2. Press `Command+Option+I` (Mac) or `Control+Shift+I` or `F12`. This should open the developer tools menu of your browser.
3. Go into the `application` section.
4. In the menu on the left go int `Storage/Cookies/open.spotify.com`.
5. Find the `sp_dc` and `sp_key` and copy the values.
6. Close the window without logging out (Otherwise the cookies are made invalid).

<img src="https://raw.githubusercontent.com/fondberg/spotcast/master/images/cookies_chrome_2.png"></img>

## 📜 License 📜

[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)   
Skyxlor is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.

<h4 align="center">Copyright (C) 2020 - 2023 <a href="https://github.com/Skyxlor">Skyxlor</a></h4>

Project [RockyX-Userbot](https://github.com/Skyxlor/RockyX-Userbot) is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.


## 🧑‍💻 Credits 🧑‍💻
* [![Skyxlor-Devs](https://img.shields.io/static/v1?label=Skyxlor&message=devs&color=critical)](https://t.me/M3_4_U)
* [Dan](https://github.com/pyrogram/) for [Pyrogram.](https://github.com/pyrogram/pyrogram)
* [Zaid](https://github.com/ITZ-ZAID/) for [Zaid-Userbot](https://github.com/ITZ-ZAID/ZAID-USERBOT)
* [mrismanaziz](https://github.com/mrismanaziz/) for [Pyroman-Userbot](https://github.com/mrismanaziz/PyroMan-Userbot)
* [UsergeTeam](https://github.com/UsergeTeam/) for [Userge](https://github.com/UsergeTeam/Userge)
* [TeamDerUntergang](https://github.com/TeamDerUntergang/) for [Telegram-SedenUserbot](https://github.com/TeamDerUntergang/Telegram-SedenUserBot)
* [TeamUltroid](https://github.com/TeamUltroid/) for [Ultroid](https://github.com/TeamUltroid/Ultroid)
