#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-04-28 23:33
# describe：
import os
from typing import Optional

from pydantic import BaseModel

from utils import u_file, u_json


class GlobalConfig(BaseModel):
    """ Global Configuration Model """
    access_token: Optional[str] = ""


# Profile path-may not exist
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_config_json_path = f"{project_dir}/config.json"
# Configuration Dictionary-Possible Empty Dictionary
_config_dict = u_json.eval_dict(u_file.read(_config_json_path))

# Global configuration object-environment variable with the highest value
g_config = GlobalConfig.parse_obj(_config_dict) if isinstance(_config_dict, dict) else GlobalConfig()

# Read the value of an environment variable-if present
g_config.access_token = os.environ.get('ACCESS_TOKEN') or g_config.access_token

# Video Temporary Cache Path
# （By default, the video cleaning step is ignored here.
# If necessary, the temporary video cleaning function is realized by yourself.）
video_cache_dir = f"{project_dir}/.cache/video"


def get_video_cache_dir(sub_dir: str) -> str:
    path = f"{video_cache_dir}/{sub_dir}"
    if not os.path.exists(path):
        os.makedirs(path)
    return path
