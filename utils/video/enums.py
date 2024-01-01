#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# author：samge
# data：2023-05-10 23:59
# describe：
from enum import Enum


class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def list_name(cls):
        return list(map(lambda c: c.name, cls))


class AudioFormatEnum(ExtendedEnum):
    none = ""
    wav = "wav"
    mp3 = "mp3"
