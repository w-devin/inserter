#!/usr/bin/env python
# encoding: utf-8
"""
@author: wangyawen
@contact: Mr.wyw@foxmail.com
@file: translator.py
@time: 8/26/2020 02:00
@desc:
"""

import json
import time


def translate(line):
    base = dict()

    for key in line:
        base[key.split('.')[-1]] = line[key]

    base['record_date'] = base['day']
    if not base['record_date'].isdigit():
        base['record_date'] = 'default'

    string_ts = base.get('ts', '')

    if len(string_ts) < 10:
        return None

    base['ts'] = time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.localtime(int(base.get('ts'))))

    return base








