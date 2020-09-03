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
from event_inserter.translator.rules import Rules


def translate(line):
    ret = list()
    base = dict()
    proof = dict()

    for key in line:

        if key.split('.')[-1] == 'proof':
            proof = line[key]
            continue

        base[key.split('.')[-1]] = line[key]

    try:
        proof = json.loads(proof)
    except Exception as e:
        print(line)
        print(e)
    else:
        for detail in proof.get('detail_list'):
            tmp = dict()
            rule = Rules.get(base.get('rule_id'))
            if not rule:
                print('no rule_id: {}'.format(base.get('rule_id')))
                break

            for key in rule['fields']:
                tmp[key + '_proof'] = detail.get(key)

            tmp['ts'] = time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.localtime(detail.get(rule['ts'])))
            ret.append(dict(base, **tmp))
    return ret








