"""Grades Calculator for 5 subjects."""

m1 = int(input("Enter marks of 1st subject:"))
m2 = int(input("Enter marks of 2nd subject:"))
m3 = int(input("Enter marks of 3rd subject:"))
m4 = int(input("Enter marks of 4th subject:"))
m5 = int(input("Enter marks of 5th subject:"))

percentage = (m1 + m2 + m3 + m4 + m5) / 5
print("Your percentage is:", percentage)

if percentage in range(90, 101):
    print("Your grade is A+")
elif percentage in range(80, 91):
    print("Your grade is A")
elif percentage in range(70, 81):
    print("Your grade is B+")
elif percentage in range(60, 71):
    print("Your grade is B")
elif percentage in range(50, 61):
    print("Your grade is C+")
elif percentage in range(40, 51):
    print("Your grade is C")
else:
    print("Your grade is D")
