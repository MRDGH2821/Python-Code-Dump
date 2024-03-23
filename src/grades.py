"""Grade Calculator."""

marks = int(input("Enter the marks of the student: "))
if marks in range(91, 101):
    print("Grade A")
elif marks in range(81, 91):
    print("Grade B")
elif marks in range(71, 81):
    print("Grade C")
elif marks in range(61, 71):
    print("Grade D")
else:
    print("Grade F")
