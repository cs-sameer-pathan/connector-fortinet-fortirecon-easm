""" Copyright start
Copyright (C) 2008 - 2024 Fortinet Inc.
All rights reserved.
FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
Copyright end """

from .get_asset_asns import get_multiple_records


def get_breaches(config, params):
    endpoint = "/easm/{org_id}/breaches"
    has_password = params.get("has_password")
    if has_password:
        params["has_password"] = has_password
    return get_multiple_records(config=config, endpoint=endpoint, params=params)


def get_breaches_by_id(config, params):
    endpoint = "/easm/{org_id}"+"/breaches/{0}".format(params.get("breach_id"))
    return get_multiple_records(config=config, endpoint=endpoint)
