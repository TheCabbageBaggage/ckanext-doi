#!/usr/bin/env python
# encoding: utf-8
"""
Created by 'bens3' on 2013-06-21.
Copyright (c) 2013 'bens3'. All rights reserved.
"""

from pylons import config
from paste.deploy.converters import asbool

ENDPOINT = 'https://mds.datacite.org'
TEST_ENDPOINT = 'https://mds.test.datacite.org'


def get_test_mode():
    """
    Get test mode as boolean
    @return:
    """
    return asbool(config.get("ckanext.doi.test_mode", True))


def get_prefix():
    """
    Get the prefix to use for DOIs
    @return: config prefix setting
    """

    return config.get("ckanext.doi.prefix")


def get_endpoint():

    """
    Get the DataCite endpoint
    @return: test endpoint if we're in test mode
    """
    return TEST_ENDPOINT if get_test_mode() else ENDPOINT
