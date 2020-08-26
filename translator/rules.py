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
    },
    '70012': {
        'fields': ["ip", "end_time", "days_of_month", "periodically", "type", "command", "days_of_week",
                   "add_current_date", "start_time", "job_time", "branch_id", "group", "status"],
        'ts': 'start_time'
    },
    '70019': {
        'fields': ["start_time", "opnum", "branch_id", "ip", "end_time", "type", "group", "status", "object", "command"],
        'ts': 'start_time'
    }
}
