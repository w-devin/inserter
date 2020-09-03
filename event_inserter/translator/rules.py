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
    },
    '70020': {
        'fields': ["start_time", "branch_id", "ip", "end_time", "classify1_id", "asset_id", "status", "command"],
        'ts': 'start_time'
    },
    '70024': {
        'fields': ["start_time", "opnum", "branch_id", "ip", "end_time", "classify1_id", "asset_id"],
        'ts': 'start_time'
    },
    '70025': {
        'fields': ["start_time", "branch_id", "ip", "end_time", "classify1_id", "asset_id"],
        'ts': 'start_time'
    },
    '160001': {
        'fields': ["filename", "count", "record_time", "url", "dst_ip", "hash", "desc"],
        'ts': 'record_time'
    },
    '160002': {
        'fields': ["filename", "count", "record_time", "url", "dst_ip", "hash", "desc"],
        'ts': 'record_time'
    },
    '160003': {
        'fields': ["filename", "count", "record_time", "url", "dst_ip", "hash", "desc", "src_ip"],
        'ts': 'record_time'
    },
    '160004': {
        'fields': ["filename", "src_ip", "record_time", "url", "dst_ip", "hash", "desc"],
        'ts': 'record_time'
    },

}
