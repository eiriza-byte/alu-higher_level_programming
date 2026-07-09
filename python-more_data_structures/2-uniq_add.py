#!/usr/bin/python3
"""Unique addition module."""
def uniq_add(my_list=[]):
    """Add all unique integers in a list, once each."""
    return sum(set(my_list))
