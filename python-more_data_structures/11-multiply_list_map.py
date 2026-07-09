#!/usr/bin/python3
"""Multiply by using map module."""
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
