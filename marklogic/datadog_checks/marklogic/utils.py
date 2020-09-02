# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from typing import Dict

from .config import Config


def is_resource_included(resource, config):
    # type: (Dict[str, str], Config) -> bool
    # If the resource is in an include filter and not in an exclude filter, return True, otherwise return False.
    for include_filter in config.resource_filters['included']:
        if include_filter.match(resource['type'], resource['name'], resource.get('group')):
            for exclude_filter in config.resource_filters['excluded']:
                if exclude_filter.match(resource['type'], resource['name'], resource.get('group')):
                    return False
            return True

    return False
