#!/usr/bin/python3
"""Defines a class and inherited class."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class."""
    if isinstance(obj, a_class):
        return True
    return False
