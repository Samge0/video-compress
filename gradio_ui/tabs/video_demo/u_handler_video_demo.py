#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-03-28 14:43
# describe：
import os
import time

from gradio_ui.g_utils import u_op_cache
from models.m_video import VideoParamCache
from utils.video import u_video

CACHE_KEY = "Video_Parameters_Cache"


def load():
    """ load cache """
    cache_dict = u_op_cache.read_cache(CACHE_KEY, {})
    request = VideoParamCache.parse_obj(cache_dict) if isinstance(cache_dict, dict) else VideoParamCache()
    return [
        request.input_path_single,
        request.input_dir,
        request.output_dir,
        request.target_bitrate,
        request.audio_separation_format,
        request.without_audio,
    ]


def handler(input_path_single, input_dir, output_dir, target_bitrate, audio_separation_format, without_audio):

    if not input_path_single and not input_dir:
        return "input_path_single and input_dir cannot be empty at the same time"

    input_path_single = u_video.format_file_path(input_path_single)
    input_dir = u_video.format_file_path(input_dir)
    output_dir = u_video.format_file_path(output_dir)

    if input_path_single and not u_video.is_support_video(input_path_single):
        return "input_path_single is not a valid video file path"

    if input_dir and not os.path.isdir(input_dir):
        return "input_dir is not a valid directory"

    if not target_bitrate:
        target_bitrate = "1M"

    request = VideoParamCache(
        input_path_single=input_path_single,
        input_dir=input_dir,
        output_dir=output_dir,
        target_bitrate=target_bitrate,
        audio_separation_format=audio_separation_format,
        without_audio=without_audio,
    )

    # cached data
    u_op_cache.save_cache(CACHE_KEY, request.__dict__)

    # traversing files handling video compression
    file_path_list = []
    if u_video.is_support_video(input_path_single):
        file_path_list.append(input_path_single)
    if os.path.isdir(input_dir):
        for file_name in os.listdir(input_dir):
            file_path_list.append(u_video.format_file_path(os.path.join(input_dir, file_name)))
    total_file_size = len(file_path_list)
    result_txt = ""
    for i in range(total_file_size):
        input_path = file_path_list[i]
        result_txt += parse_video_compress(i, total_file_size, target_bitrate, input_path, output_dir)

    result_txt += "all done"
    return result_txt


def parse_video_compress(i, total_file_size, target_bitrate, input_path, output_dir):
    if not u_video.is_support_video(input_path):
        return ""
    start_time = time.time()
    print(f"[{i + 1}/{total_file_size}] Processing：{input_path}")
    output_dir = output_dir or '/'.join(input_path.split('/')[:-1])
    output_path = f"{output_dir}/{u_video.get_filename(input_path)}-compress-{target_bitrate}-{u_video.get_custom_date_format()}.mp4"
    u_video.compress_video(input_path, output_path, target_bitrate=target_bitrate)
    all_time = time.time() - start_time
    return f"""[{i + 1}/{total_file_size}]
Total consumption：{all_time:.2f}s
input：
    - path：{input_path}
    - size：{u_video.get_file_size_mb(input_path):.2f}M
output：
    - path：{output_path}
    - size：{u_video.get_file_size_mb(output_path):.2f}M
    
"""
