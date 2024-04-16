"""Products of elements of a list."""

from __future__ import annotations

from secrets import randbelow

random_numbers = [randbelow(50) for _ in range(10)]
print(random_numbers)


def multiply_list_elements(g: list[int]) -> int:
    """Return the product of all elements of a list."""
    prd = 1
    for d in g:
        prd = prd * d
    return prd


print("Product of elements of list =", multiply_list_elements(random_numbers))
