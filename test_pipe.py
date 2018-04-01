#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pipe


def test_filter_top_domain_name():
    domain = ["[2018-04-01T14:11:38.783874] ct.googleapis.com/logs/argon2018/ - docs-beta.monetizesocial.com",
              "[2018-04-01T14:11:40.243578] ct.googleapis.com/icarus/ - www.witze-dschungel.lima-city.de",
              "[2018-04-01T14:11:40.184876] ct.googleapis.com/icarus/ - sallesdevillefagnan.fr"]

    assert pipe.filter_top_domain_name(domain[0]) == "com"
    assert pipe.filter_top_domain_name(domain[1]) == "de"
    assert pipe.filter_top_domain_name(domain[2]) == "fr"


def test_create_statistics():
    top_domains = ["com", "com", "de", "fi", "com", "cz", "de"]

    statistics_dic = {"com": 3, "de": 2, "fi": 1, "cz": 1}

    for value in top_domains:
        pipe.create_statistics(value)

    assert pipe.create_statistics(None, return_only=True) == statistics_dic


def test_clean_string():
    test_string = "ca\x1b[0m \n"

    assert pipe.clean_string(test_string) == "ca"


def test_display_statistics():
    pass
