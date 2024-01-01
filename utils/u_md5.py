#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/4/19 下午7:25
# @Author  : Samge
import hashlib


"""
built in md 5 generation tool class
"""


def create_md5(v: str, with_csharp: bool = False) -> str:
    """
    generate 32 bit length md 5
    :param v:
    :param with_csharp: Is it compatible with md 5 on the other side of the c# project
    :return:
    """
    if not with_csharp:
        return hashlib.md5(v.encode('utf-8')).hexdigest() if v else None
    try:
        return hashlib.md5(v.encode('GBK')).hexdigest() if v else None
    except Exception as e:
        return hashlib.md5(v.encode('utf-8')).hexdigest() if v else None


if __name__ == '__main__':
    print(create_md5("test"))
