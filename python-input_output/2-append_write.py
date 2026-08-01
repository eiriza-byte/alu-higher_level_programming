#!/usr/bin/python3
"""Module that appends a string to the end of a text file."""


def append_write(filename="", text=""):
    """Append a string at the end of a text file, return chars added."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
