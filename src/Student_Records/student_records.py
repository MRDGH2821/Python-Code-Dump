"""Student Records.

Keeps a record of class students.
Records consist of student's name, roll number, and marks in 3 subjects.
"""

from __future__ import annotations

import os
from pathlib import Path
from time import sleep

# Initialising variables
name = ""
m1 = 0
m2 = 0
m3 = 0
roll_no = 0
with Path("students.txt").open("a+") as f:
    print("Ensuring that the file exists")


def remove_blank_lines(filename: str) -> None:
    """Remove blank lines from a file."""
    with Path(filename).open() as in_file:
        lines = in_file.readlines()

    non_blank_lines = [line for line in lines if line.strip()]

    with Path(filename).open("w") as out_file:
        out_file.writelines(non_blank_lines)


# Usage
remove_blank_lines("students.txt")


def takedata() -> list[int | str]:
    """Take data from user."""
    name = str(input("Enter Name:"))
    m1 = int(input("Enter marks out of 100 in subject 1:"))
    m2 = int(input("Enter marks out of 100 in subject 2:"))
    m3 = int(input("Enter marks out of 100 in subject 3:"))
    roll_no = int(input("Enter Roll no.:"))
    return [roll_no, name, m1, m2, m3]


def writedata() -> None:
    """Write Data into file."""
    # opening file in append as well as write mode.
    with Path("student.txt").open("a+") as f:
        f.write("\n")  # A precautionary new line
        lt = takedata()  # calling takedata function
        for v in lt:  # writing data to file
            f.write(str(v) + " ")
    input("Data entered. Press enter key to continue...")
    menu()  # calling menu function


def readall() -> None:
    """Read complete data."""
    with Path("student.txt").open() as j:  # opening file
        lk = j.readlines()  # reading complete data
        print(
            "{:6} {:4} {:4} {:4} {:4}".format(
                "Roll no",
                "Name",
                "Sub1",
                "Sub2",
                "Sub3",
            ),
        )
        # printing data in formatted form
        for c in range(len(lk)):
            c1 = lk[c].split()
            print(
                f"{c1[0]:^6} {c1[1]:^4} {c1[2]:^4} {c1[3]:^4} {c1[4]:^4}",
            )

    input("\nPress enter key to continue...")
    menu()  # calling menu function


def readspecific() -> None:
    """Retrieve specific data from file."""
    with Path("student.txt").open() as k:  # opening file
        g = k.readlines()  # reading complete file
        roll_no = input("Enter Roll no:")  # Taking roll no as user input
        flag = 0  # flag to denote whether data is found or not
        for h in g:  # looping through data
            try:
                """
                Here, the format of data is - roll no name m1 m2 m3.
                Hence we need to split the elements of data (read as lines),
                Find the roll number and
                display the data associated with the roll number.
                """
                i = h.split()
                if roll_no == i[0]:  # Condition to find roll number
                    # per =(i[1]+i[2]+i[3])/3
                    # Formatting output
                    print(
                        "{}\n{}\n{}\n{}\n{}".format(
                            "Roll no:" + i[0],
                            "Name:" + i[1],
                            "Sub1:" + i[2],
                            "Sub2:" + i[3],
                            "Sub3:" + i[4],
                        ),
                    )
                    flag = 1  # flagging as data found
            except IndexError:
                # This error comes when a list of empty line is accessed using
                # index slicing. Empty line create empty list
                # this error is hidden using continue statement.
                continue
            if flag == 0:
                print("Roll no not found")
    k.close()  # Closing file
    input("\nPress enter key to continue...")
    menu()


def deletedata() -> None:
    """Delete data of specified roll number."""
    # flag to denote whether data is found or not
    flag = 0
    with Path("student.txt").open() as data:
        # Reading complete data
        j = data.readlines()

        # Taking roll number as input
        roll_no = input("Enter Roll no:")

        # Opening a temporary file to store data
        with Path("temp.txt").open("w") as l2:
            for h in range(len(j)):
                """
                Here, the format of data is - Roll no name m1 m2 m3.
                Hence we need to split the elements of data (read as lines),
                find the roll number and
                delete the data associated with the roll number.
                """
                if flag == 1:
                    # Coming out of loop after the data is deleted
                    break
                try:
                    i = j[h].split()
                    # Condition to find roll number
                    if roll_no == i[0]:
                        # deleting data
                        del j[h]
                        # writing leftover data to temp file
                        l2.writelines(j)
                        # flagging as data found
                        flag = 1

                    else:
                        # Raise LookupError because data wasn't found
                        raise LookupError
                except IndexError:
                    # This error comes when a list of empty line is accessed using
                    # index slicing. Empty line create empty list
                    # this error is hidden using continue statement.
                    continue
                except LookupError:
                    # flagging as data not found
                    flag = 0
    # Flag checker to check if data deleted or not
    if flag == 0:
        print("Record not found")
    elif flag == 1:
        print("Record Deleted")
        # closing files
    data.close()
    l2.close()
    # deleting the old file
    Path("student.txt").unlink()
    # renaming temp file to original file name
    Path("temp.txt").rename("student.txt")
    input("\nPress enter key to continue...")
    menu()


def backup() -> None:
    """Back up the data file."""
    with Path("student.txt").open() as f, Path("student bkp.txt").open("w") as g:
        # Copying contents of original file into backup file
        g.writelines(f.readlines())

    print("Backup Completed!")
    sleep(2)  # delays execution for 2 seconds


def menu() -> None:
    """Show menu."""
    backup()
    os.system("cls")
    print("\nMenu:")
    print("1. Create student record")
    print("2. See all student records")
    print("3. Find Specific record")
    print("4. Delete specific data")
    # print("5. Sort data (Will close program after sorting)")
    # i.e. manually backing up data
    print(" - 1. Force Backup data(Will close program after backup) ")
    print("0. Exit")
    print("")
    print("*Note: The data file is back-ed up at menu screen\n")
    m = int(input("Your Input:"))
    try:
        if m == 0:
            raise SystemExit  # Raises SystemExit to terminate the program
        elif m == -1:
            backup()
        elif m == 1:
            writedata()
        elif m == 2:  # noqa: PLR2004
            readall()
        elif m == 3:  # noqa: PLR2004
            readspecific()
        elif m == 4:  # noqa: PLR2004
            deletedata()
        else:
            # Raises ValueError as the input received is not from
            # [-1,0,1,2,3,4]
            raise ValueError
    except ValueError:
        print("Invalid choice")
    except SystemExit:
        print("Program Closed")


# Intro Screen
print(
    "\n{:^50}\n\n\n{:^50}".format(
        "Student Records",
        "Project made by: MRDGH2821",
    ),
)
sleep(3)
print("\n\n\n")
menu()
