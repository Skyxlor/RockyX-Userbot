# Copyright (C) 2020-2023 Skyxlor <https://github.com/Skyxlor>
#
# This file is part of Skyxlor project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# Developer Credits: @M3_4_U

from RockyX import *
from RockyX.lib import *
import requests
import os

async def tiktok_downloader(client, message):
    ran = await message.reply_text("<code>Processing.....</code>")
    link = message.text.split(None, 1)[1] if len(message.command) !=1 else None
    if not link:
        await ran.edit_text("please for example the TikTok link here")
        return

    url = "https://tiktok-full-info-without-watermark.p.rapidapi.com/vid/index"
    querystring = {"url": link}

    headers = {"X-RapidAPI-Key": "ce36c261f1mshb4a0a55aaca548ep12c9f3jsn3d6761cb63fb", "X-RapidAPI-Host": "tiktok-full-info-without-watermark.p.rapidapi.com"}

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        data_response = response.json()
        try:
            music_urls = data_response["music"]
            video_urls = data_response["video"]
        except Exception as e:
            await ran.edit_text(f"Error request {e}")
            return
        
        for video_url in video_urls:
            video_response = requests.get(video_url)
        for music_url in music_urls:
            music_response = requests.get(music_url)
        
        if music_urls and video_urls:
            if video_response:
                send_video_file_path = "RockyX_userbot.mp4"
                with open(send_video_file_path, "wb") as f:
                    f.write(video_response.content)
                await client.send_video(message.chat.id, video=send_video_file_path, reply_to_message_id=message.id)
                os.remove(send_video_file_path)
            elif music_response:
                send_audio_file_path = "RockyX_userbot.mp3"
                with open(send_audio_file_path, "wb") as f:
                    f.write(music_response.content)
                await client.send_audio(message.chat.id, audio=send_audio_file_path, reply_to_message_id=message.id)
                os.remove(send_audio_file_path)
            else:
                await ran.edit_text("Error please try again")
        else:
            await ran.edit_text("Error please try again tiktok")
    else:
        await ran.edit_text("Error failed api TikTok")
    try:
        await ran.delete()
    except Exception:
        pass

async def tiktok_downloader_2(client, message):
    ran = await message.reply_text("<code>Processing.....</code>")
    link = message.text.split(" ", 1)[1] if len(message.command) !=1 else None
    if not link:
        await ran.edit_text("please for example the TikTok link here")
        return

    url = "https://tiktok-downloader-without-watermark-api-download-tiktok-videos.p.rapidapi.com/"

    payload = { 
        "URL": link,
        "type": "video",
        "file": "mp4",
        "quality": "NO Watermark",
        "mute": False
    }

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "ce36c261f1mshb4a0a55aaca548ep12c9f3jsn3d6761cb63fb",
        "X-RapidAPI-Host": "tiktok-downloader-without-watermark-api-download-tiktok-videos.p.rapidapi.com"
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        data = response.json()
        try:
            duration = data["duration"]
            video_url = data["links"][0]["url"]
        except Exception as e:
            await ran.edit_text(f"Error request {e}")
            return

        video_urls = requests.get(video_url)
        if video_url:
            if video_urls:
                send_video_path = "video.mp4"
                with open(send_video_path, "wb") as f:
                    f.write(video_urls.content)
                await client.send_video(message.chat.id, video=send_video_path, reply_to_message_id=message.id)
                os.remove(send_video_path)
            else:
                await ran.edit_text("Error please try again")
        else:
            await ran.edit_text("Error please try again tiktok")
    else:
        await ran.edit_text("Error failed api TikTok")
    try:
        await ran.delete()
    except Exception:
        pass
