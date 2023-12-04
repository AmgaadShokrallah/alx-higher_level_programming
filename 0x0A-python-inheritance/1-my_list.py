#!/usr/bin/python3
"""Defines class MyList."""


class MyList(list):
    """printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ."""
        print(sorted(self))
