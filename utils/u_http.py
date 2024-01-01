#!/usr/bin/ruby
# -*- coding : utf-8 -*-
# author：samge
# data：2023-02-28 14:56
# describe：


def common_response(code, data, msg) -> dict:
    """
    Unified reply format
    :param code: Response Code
    :param data: Data
    :param msg: Prompt Message
    :return:
    """
    return {
        'code': code,
        'data': data,
        'msg': msg,
    }


def success(data) -> dict:
    """
    Successful response
    :param data:
    :return:
    """
    return common_response(200, data, 'success')


def fail400(msg: str = 'Parameter error') -> dict:
    """ Failed response """
    return common_response(400, None, msg)


def fail403(msg: str = 'Permission verification failed') -> dict:
    """ Permission verification failed """
    return common_response(403, None, msg)


def fail500(msg: str = 'Service exception, please try again later') -> dict:
    """ Service Error """
    return common_response(500, None, msg)
