#!/usr/bin/ruby
# -*- coding : utf-8 -*-
# author：samge
# data：2023-02-28 15:11
# describe：
from typing import Optional

from pydantic import BaseModel


class VideoParamCache(BaseModel):
    filename: Optional[str] = None
    input_path_single: Optional[str] = None
    input_dir: Optional[str] = None
    output_dir: Optional[str] = None
    target_bitrate: Optional[str] = '1M'
    audio_separation_format: Optional[str] = None
    without_audio: Optional[bool] = False


