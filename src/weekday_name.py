"""Weekday Name.

Determines the name of given day number.
"""

from enum import Enum


class Weekdays(Enum):
    """Enum class for weekdays."""

    Sunday = 0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6

    @classmethod
    def print_day(cls, date: int) -> str:
        """Print the name of the day of the week."""
        name = "Invalid Number"
        for day in cls:
            if date % 7 == day.value:
                name = day.name
                break
        return name


day = int(input("Enter day number: "))
print(Weekdays.print_day(day))
