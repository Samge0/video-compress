#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-03-28 11:38
# describe：
import json
import os

from utils import u_json, u_file

"""
operation related caching tools
"""


project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
cache_dir = f'{project_dir}/.cache/gradio_cache/operation_cache'


def __init_cache_dir():
    """ initialize cache directory """
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)


def save_cache(key: str, value):
    """
    save general cache data
    :param key:
    :param value:
    :return:
    """
    path = __get_common_cache_path()
    current_cache_dict = u_json.eval_dict(u_file.read(path))
    current_cache_dict[key] = value
    txt = json.dumps(current_cache_dict, ensure_ascii=False, indent=4).encode('utf-8')
    txt = str(txt, encoding='utf-8')
    u_file.save(txt, path)
    print(f"【{key}】缓存保存在：{path}")


def read_cache(key: str, default_value):
    """
    read general cache data
    :param key:
    :param default_value:
    :return:
    """
    path = __get_common_cache_path()
    current_cache_dict = u_json.eval_dict(u_file.read(path))
    return current_cache_dict.get(key) or default_value


def __get_common_cache_path() -> str:
    """
    get general cache file path
    :return:
    """
    __init_cache_dir()
    return f'{cache_dir}/common_cache.json'


def __get_url(request, is_dtl: bool) -> str:
    return request.url_dtl if is_dtl else request.url_lst
