"""List of Squares.

Prints all the squares of numbers from 0 to a given number.
"""

from __future__ import annotations


def sq_list(j: int) -> list[int]:
    """Return list of squares of numbers from 0 to j."""
    return [g**2 for g in range(j + 1)]


a = int(input("Input a number:"))
print(sq_list(a))
