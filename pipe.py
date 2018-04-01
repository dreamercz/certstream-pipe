#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script takes piped input, filters and processes it, and displays statistics about the piped data.
Based on the workshop assigment from: https://github.com/intraworlds/workshop-php
"""

import sys

domain_stats = {}


def filter_top_domain_name(line):
    # Filter full domain name from the entire line
    full_domain_name = line.split(" - ")[1]
    # Filter out only the top level domain
    top_domain = full_domain_name.split(".")[-1]

    return top_domain


def create_statistics(top_domain, return_only=False):
    # If True, returns the current statistic dictionary (for tests)
    if return_only is True:
        return domain_stats
    # If key already exists, increase it's count
    if top_domain in domain_stats:
        domain_stats[top_domain] += 1
        return domain_stats
    # If key didn't exist before, save it as new occurence
    domain_stats[top_domain] = 1

    return domain_stats


def display_statistics():
    pass


def main(line):
    line = filter_top_domain_name(line)
    create_statistics(line)


if __name__ == '__main__':
    for line in sys.stdin:
        main(line)
