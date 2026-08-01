#!/usr/bin/python3
"""Module that returns the dictionary description of an object."""


def class_to_json(obj):
    """Return a dict description of obj for JSON serialization."""
    return obj.__dict__
