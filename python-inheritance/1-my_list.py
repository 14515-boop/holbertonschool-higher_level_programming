#!/usr/bin/python3
"""Module that defines MyList."""


class MyList(list):
    """Custom list that can print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))
