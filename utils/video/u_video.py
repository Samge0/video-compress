#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-04-28 23:59
# describe：
import os
import time
from datetime import datetime

from moviepy.editor import VideoFileClip

from utils import u_file


def compress_video(
        input_path,
        output_path,
        target_bitrate='1M',
        audio_separation_format=None,
        without_audio=False
) -> str:
    """
    compress_video

    :param input_path:  video paths that require compression
    :param output_path: save path after compression
    :param target_bitrate:
        If your video needs to be played on a mobile device, you also need to consider the trade-off between video quality and file size. Depending on the device and network speed, the recommended bit rate range is 1-2 Mbps.
        If you need to upload a video to a video website, such as YouTube, it is recommended that the compressed bit rate is 4-6 Mbps (that is, 4-6 Mbit/s), which can ensure high-quality video and small file size. This is also the YouTube recommend bit rate range. Exceeding this range may cause the compressed video quality to deteriorate or the upload speed to slow down.
        The higher the compressed bit rate, the better the video quality, but the larger the file size. Therefore, you need to weigh the bitrate and file size according to your actual needs to achieve the best results.
    :param audio_separation_format: The audio format that needs to be separated. Currently, only wav and mp 3 are supported.(save a separate audio file)
    :param without_audio:   Whether to remove compressed video and audio (mute)

    :return: output_path
    """
    video = VideoFileClip(input_path)

    if video.audio is not None:

        if audio_separation_format:
            audio_clip = video.audio
            if 'wav' == audio_separation_format:
                audio_clip.write_audiofile('.'.join(output_path.split('.')[:-1]) + '.wav')
            else:
                audio_clip.write_audiofile('.'.join(output_path.split('.')[:-1]) + '.mp3', codec='mp3')

        if without_audio:
            video = video.without_audio()

    video.write_videofile(output_path, codec='libx264', audio_bitrate=target_bitrate, fps=video.fps, audio_codec='aac')
    return output_path


def get_file_size_mb(file_path) -> float:
    file_size_bytes = os.path.getsize(file_path)
    return file_size_bytes / (1024 * 1024)


def get_custom_date_format(f: str = "%Y%m%d-%H%M%S") -> str:
    now = datetime.now()
    return now.strftime(f)


def get_filename(filepath) -> str:
    if filepath and os.path.exists(filepath):
        return os.path.basename(filepath).split('.')[0]
    else:
        return ""


def is_support_video(filepath) -> str:
    return filepath.endswith(".mp4") or filepath.endswith(".avi")


def format_file_path(filepath) -> str:
    return (filepath or "").replace(os.sep, "/")


def check_video_file(file_obj) -> str:
    """
    check whether the file meet the requirements
    :param file_obj:
    :return:
    """
    suffix_str = 'mp4、avi'
    if not file_obj:
        return f"Please upload the file with the suffix {suffix_str}"

    filename = file_obj.name or ''
    if not is_support_video(filename):
        return f"Please upload the file with the suffix {suffix_str}"

    if not u_file.exists(filename):
        return "During file upload, please wait for the file to be uploaded before operating"

    return None


def _test():
    start_time = time.time()

    target_bitrate = '1M'
    input_dir = '/xxx/xxx'
    input_path = f'{input_dir}/xxx.mp4'
    output_path = f'{input_dir}/compress-result-{target_bitrate}-{get_custom_date_format()}.mp4'
    compress_video(input_path, output_path, target_bitrate=target_bitrate)

    all_time = time.time() - start_time

    result_txt = f"""Total consumption：{all_time:.2f}s
Original video size：{get_file_size_mb(input_path):.2f}M
Size after compression：{get_file_size_mb(output_path):.2f}M
output_path：{output_path}
"""
    print(result_txt)


if __name__ == '__main__':
    _test()
    pass
