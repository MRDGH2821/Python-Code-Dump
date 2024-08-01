"""
The question:
You have recently seen a motivational sports movie and want to start exercising regularly.
Your coach tells you that it is important to get up early in the morning to exercise. 
She sets up a schedule for you:

On weekdays (Monday - Friday), you have to get up at 5:00. On weekends (Saturday & Sunday), you can wake up at 6:00.
However, if you are on vacation, then you can get up at 7:00 on weekdays and 9:00 on weekends.

Write a program to print the time you should get up.

Input Format

The first line contains n - the number of inputs.
Following that are n lines, each containing an integer and a boolean value.

The integer tells you the day it is (1-Sunday, 2-Monday, 3-Tuesday, 4-Wednesday, 5-Thursday, 6-Friday, 7-Saturday).
The boolean is true if you are on vacation and false if you’re not on vacation.

You have to print the time you should get up.

You have to write the entire program and not just the method. Please keep the name of your class as Main

Example Input:
3
1 false
5 false
1 true
Output:
6:00
5:00
9:00
"""


def Main(day, boolean):
    if boolean == "true" and (day == 1 or day == 7):
        print("9:00")
    elif boolean == "true" and day in range(2, 6):
        print("7:00")
    elif boolean == "false" and day in range(2, 6):
        print("5:00")
    else:
        print("6:00")


i = 1
n = int(input())

while (i <= n):
    inp = input().split()
    day = int(inp[0])
    bool = inp[1]

    Main(day, bool)
    i = i + 1
