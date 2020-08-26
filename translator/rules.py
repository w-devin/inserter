#!/usr/bin/env python
# encoding: utf-8
"""
@author: wangyawen
@contact: Mr.wyw@foxmail.com
@file: rules.py
@time: 8/26/2020 02:06
@desc:
"""

Rules = {
    '70011': {
        'fields': ["service_name", "ip", "end_time", "display_name", "type", "start_time", "service_type",
                   "branch_id", "opnum", "service_start_type", "group", "status", "binary_path_name"],
        'ts': 'start_time'
    }
}
