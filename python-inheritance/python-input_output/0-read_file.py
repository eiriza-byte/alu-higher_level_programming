#!/usr/bin/python3
"""Module that reads a text file and prints its content."""


def read_file(filename=""):
    """Read a text file (UTF8) and print it to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
