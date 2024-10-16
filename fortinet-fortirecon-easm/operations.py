""" Copyright start
Copyright (C) 2008 - 2024 Fortinet Inc.
All rights reserved.
FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
Copyright end """


from .get_leaked_credentials import get_leaked_credentials
from .get_scan_statistics import get_scan_statistics
from .issues import *
from .get_asset_asns import *
from .get_breaches import get_breaches, get_breaches_by_id
from .generate_report import generate_report, get_report

operations = {
    "get_leaked_credentials": get_leaked_credentials,
    "get_archived_issues": get_archived_issues,
    "get_issue_summary": get_issue_summary,
    "get_scan_statistics": get_scan_statistics,
    "get_issue_by_id": get_issue_by_id,
    "get_issues_discovered": get_issues_discovered,
    "get_asset_asns": get_asset_asns,
    "get_asns_by_asset_id": get_asns_by_asset_id,
    "get_domains": get_domains,
    "get_domain_by_asset_id": get_domains_by_asset_id,
    "get_ips": get_ips,
    "get_ips_by_asset_id": get_ips_by_asset_id,
    "get_prefixes": get_prefixes,
    "get_prefixes_by_asset_id": get_prefixes_by_asset_id,
    "get_subdomains": get_subdomains,
    "get_subdomain_by_asset_id": get_subdomains_by_asset_id,
    "get_asset_statistics": get_asset_statistics,
    "get_breaches": get_breaches,
    "get_breaches_by_id": get_breaches_by_id,
    "generate_report": generate_report,
    "get_report": get_report,
    "get_archived_assets": get_archived_assets,
    "get_exposed_services": get_exposed_services,
    "get_cloud_integrations": get_cloud_integrations,
    "get_fgt_integrations": get_fgt_integrations,
    "get_security_insights": get_security_insights,
    "get_archived_issue_comments": get_archived_issue_comments,
    "get_issue_comments": get_issue_comments,
    "get_tags": get_tags,
    "get_tag_by_id": get_tags,
    "get_groups": get_groups,
    "get_group_by_id": get_groups

}
