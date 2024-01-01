#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 下午4:45
# @Author  : Samge


"""
The "safe" json character to dictionary object tool class, the "safe" is sponsored by try except title......
"""


null, false, true = None, False, True


def eval_dict(v: str, default_value: dict = {}) -> dict:
    """
    Here, eval is treated uniformly for null, false and true, which are worth parsing.
    :param v:
    :param default_value:
    :return:
    """
    try:
        return eval(v)
    except Exception as e:
        return default_value
