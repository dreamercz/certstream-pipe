#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script takes piped input from the cerstream script, filters and processes it,
and displays real-time statistics about the top 10 used top level domains sorted in descending order
by the number of the occurences of the domain name.

Adapted from the IntraWorlds PHP workshop assigment from: https://github.com/intraworlds/workshop-php

Usage: $ certstream | python3 pipe.py
"""

import sys
import re

# Used to store domian names and number of occurences.
# Must be global so the dictionary is persistent and accessible by unit tests.
domain_stats = {}


def filter_top_domain_name(line):
    """Takes the line from stdin and filters out only the last part,
    which is the full domain name. Then it strips that so only the top level
    domain name is returned.

    Arguments:
        line {string} -- The whole line as piped in from the certstream script.

    Returns:
        top_domain {string} -- Top level domain name, eg. "com", "net" etc.
    """
    # Filter full domain name from the entire line
    full_domain_name = line.split(" - ")[1]
    # Filter out only the top level domain
    top_domain = full_domain_name.split(".")[-1]

    return top_domain


def clean_string(dirty_string):
    """Cleans the retrieved top level domain string from any ANSI escape
    sequences as well as empty spaces and newlines.

    Arguments:
        dirty_string {string} -- Top level domain string with the unwanted characters.

    Returns:
        new_string {string} -- Clenaed up string containing only top level domain name.
    """
    # Removes ansi escape sequences
    new_string = re.sub(u"\u001b\[.*?[@-~]", "", dirty_string)
    # Removes newline and empty space
    new_string = new_string.replace("\n", "").replace(" ", "")

    return new_string


def create_statistics(top_domain, return_only=False):
    """Inserts the domain name into the global domain_stats dictionary.
    In case the domain name already exists in the dictionary, it increases it's value by 1.

    Arguments:
        top_domain {string} -- The top level domain name.

    Keyword Arguments:
        return_only {bool} -- If True, fn returns global dict without inserting new domain. (default: {False})

    Returns:
        domain_stats {dictionary[str, int]} -- Dictionary of domain names and the number of occurences.
    """
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


def sort_domains(unsorted_domains):
    """Takes unsorted dictionary of domains and occurences and sorts them according to their number of occurences.

    Arguments:
        unsorted_domains {dictionary[str, int]} -- Unsorted dictionary of domain names and number of occurences.

    Returns:
        sorted_domains {list[tuple(str, int)]} -- List of domain and occurences pairs sorted in descending order.
    """
    # Sorts domains by occurence, returns list of values
    sorted_counts = sorted(unsorted_domains.values(), reverse=True)
    # Sorts domains by occurence, but returns keys instead of values
    sorted_keys = sorted(unsorted_domains, key=unsorted_domains.__getitem__, reverse=True)
    # Packs everything together again
    sorted_domains = zip(sorted_keys, sorted_counts)

    return sorted_domains


def display_top_ten(sorted_domains):
    """Unpacks the zipped list of tuples and displays it as a table of top 10 used domains.

    Arguments:
        sorted_domains {list[tuple(str, int)]} -- Domains and occurences sorted in descending order.
    """
    # Unpack the zip, only up to ten items
    pairs = []
    for _, pair in zip(range(10), sorted_domains):
        pairs.append(pair)
    # Print tuples from the list in a nice little table
    for tup in pairs:
        print("{0}    {1}".format(*tup))
    print("\n")


def main(line):
    line = filter_top_domain_name(line)  # Takes the string piped from stdin
    line = clean_string(line)  # Cleans the string of any unwanted characters and escape sequences
    stats = create_statistics(line)  # Adds domain name to dictionary, counts number of occurences
    domains = sort_domains(stats)  # Sorts the domain names by their number of occurences
    display_top_ten(domains)  # Displays top 10 domains in descending order


if __name__ == '__main__':
    for line in sys.stdin:
        main(line)
