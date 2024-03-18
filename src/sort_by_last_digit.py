"""Sort by last digit."""

from __future__ import annotations

from random import randint

numbers = [randint(1, 1000) for _ in range(10)]  # noqa: S311


def sort_by_comprehension() -> None:
    """Use list comprehension to sort the numbers by their last digit."""
    sorted_numbers = [i for i in numbers if i == i % 10]
    sorted_numbers.sort()
    print(sorted_numbers)


def sort_by_lambda() -> None:
    """Use lambda to sort the numbers by their last digit."""
    sorted_numbers: list[int] = []
    sorted_numbers.extend(numbers)
    sorted_numbers.sort(key=lambda x: x % 10, reverse=False)
    print(sorted_numbers)


def sort_by_maths() -> None:
    """Use maths to sort the numbers by their last digit."""
    sorted_numbers = [x % 10 for x in numbers]
    sorted_numbers.sort()
    print(sorted_numbers)


def sort_by_last_character() -> None:
    """Use string manipulation to sort the numbers by their last digit."""
    sorted_numbers = [str(i)[::-1] for i in numbers]
    sorted_numbers.sort()
    print(sorted_numbers)


if __name__ == "__main__":
    print("Original list:\n", numbers)

    print("\nSort by Comprenhension:")
    sort_by_comprehension()

    print("\nSort by Lambda:")
    sort_by_lambda()

    print("\nSort by Maths:")
    sort_by_maths()

    print("\nSort by Last Character:")
    sort_by_last_character()
