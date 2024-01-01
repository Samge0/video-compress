#!/usr/bin/ruby
# -*- coding : utf-8 -*-
# author：samge
# data：2023-05-10 20:56
# describe：
import os

from fastapi import Depends, FastAPI, Header, UploadFile, File

from models.m_video import VideoParamCache
from utils import u_http, u_config
from utils.u_config import g_config
from utils.video import u_video


async def verify_token(Authorization: str = Header(...)):
    """ token simple authentication """
    if g_config.access_token and f"Bearer {g_config.access_token}" != Authorization:
        print(f"Authentication failed：{Authorization}")
        u_http.fail403(msg='Authorization header invalid')


app = FastAPI(dependencies=[Depends(verify_token)])


# video upload
@app.post("/api/video/upload")
async def api_video_upload(file: UploadFile = File(...)):
    # Save video to cache directory
    video_cache_path = f"{u_config.get_video_cache_dir('upload')}/{file.filename}"
    with open(video_cache_path, "wb") as f:
        while True:
            chunk = await file.read(1024)  # 1024 bytes per read
            if not chunk:
                break
            f.write(chunk)

    # Determine that the video is saved successfully and start to compress it.
    if os.path.exists(video_cache_path):
        return u_http.success(file.filename)
    else:
        return u_http.fail500()


# video compression
@app.post("/api/video/compress")
async def api_video_compress(request: VideoParamCache):
    input_path_single = f"{u_config.get_video_cache_dir('upload')}/{request.filename}"
    if os.path.exists(input_path_single):
        # After compression, return to the video download path and clear the original video
        output_path = f"{u_config.get_video_cache_dir('compress')}/{u_video.get_filename(input_path_single)}.mp4"
        result = u_video.compress_video(
            input_path_single,
            output_path,
            target_bitrate=request.target_bitrate,
            audio_separation_format=request.audio_separation_format,
            without_audio=request.without_audio
        )
        return u_http.success(result)
    else:
        return u_http.fail500()
