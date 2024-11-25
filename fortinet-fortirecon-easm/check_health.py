""" Copyright start
Copyright (C) 2008 - 2024 Fortinet Inc.
All rights reserved.
FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
Copyright end """

from .scan_statistics import get_scan_statistics


def check_health_ex(config):
    get_scan_statistics(config, {})
    return True
