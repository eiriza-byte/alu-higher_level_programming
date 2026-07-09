#!/usr/bin/python3
"""Module that defines safe_print_integer."""


def safe_print_integer(value):
    """Print an integer using {:d}.format() and return True on success."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
