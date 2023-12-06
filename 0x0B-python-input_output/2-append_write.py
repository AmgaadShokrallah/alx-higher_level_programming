#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends UTF8 text file."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
