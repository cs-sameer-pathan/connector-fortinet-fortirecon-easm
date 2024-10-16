""" Copyright start
Copyright (C) 2008 - 2024 Fortinet Inc.
All rights reserved.
FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
Copyright end """

from .make_rest_api_call import MakeRestApiCall
from datetime import datetime


def get_leaked_credentials(config, params):
    MK = MakeRestApiCall(config=config)
    endpoint = "/easm/{org_id}/leaked_creds"
    start = params.get("start_date")
    if start:
        params["start_date"] = datetime.strptime(start.strip('Z'), "%Y-%m-%dT%H:%M:%S.%f").strftime("%Y-%m-%d")
    end = params.get("end_date")
    if end:
        params["end_date"] = datetime.strptime(end.strip('Z'), "%Y-%m-%dT%H:%M:%S.%f").strftime("%Y-%m-%d")
    has_password = params.get("has_password")
    if isinstance(has_password, bool):
        params["has_password"] = "true" if has_password else "false"
    payload = MK.build_payload(params)
    response = MK.make_request(endpoint=endpoint, method="GET", params=payload)
    return response

