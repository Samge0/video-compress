#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-04-28 23:59
# describe：
import os

from utils import u_file

# cache directory name
cache_dir_name = '.cache'


def _get_project_dir() -> str:
    """ get project directory """
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_cache_dir() -> str:
    """ initialize cache directory """
    cache_dir = f"{_get_project_dir()}/{cache_dir_name}"
    u_file.makedirs(cache_dir)
    return cache_dir


def save(filename: str, txt: str) -> str:
    """
    save cache
    :param filename: cache file name
    :param txt: caching text content
    :return: Save successfully = returns the cache file path,
             Save failed = None
    """
    file_path = f"{get_cache_dir()}/{filename}"
    return file_path if u_file.save(txt, file_path) else None


def get(filename: str, default_value: str) -> str:
    """
    read cache
    :param filename: cache file name
    :param default_value: default value
    :return:
    """
    file_path = f"{get_cache_dir()}/{filename}"
    return u_file.read(file_path) or default_value
