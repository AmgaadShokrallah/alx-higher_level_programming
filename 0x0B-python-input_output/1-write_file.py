#!/usr/bin/python3
"""Defines a text file line."""


def number_of_lines(filename=""):
    """Returns the number of lines in a text file."""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines
