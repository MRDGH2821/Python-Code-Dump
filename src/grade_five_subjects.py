m1 = int(input("Enter marks of 1st subject:"))
m2 = int(input("Enter marks of 2nd subject:"))
m3 = int(input("Enter marks of 3rd subject:"))
m4 = int(input("Enter marks of 4th subject:"))
m5 = int(input("Enter marks of 5th subject:"))
percentage = (m1 + m2 + m3 + m4 + m5) / 5
print("Your percentage is:", percentage)
if percentage >= 90:
    print("Your grade is A+")
elif percentage >= 80 and percentage < 90:
    print("Your grade is A")
elif percentage >= 70 and percentage < 80:
    print("Your grade is B+")
elif percentage >= 60 and percentage < 70:
    print("Your grade is B")
elif percentage >= 50 and percentage < 60:
    print("Your grade is C+")
elif percentage >= 40 and percentage < 50:
    print("Your grade is C")
else:
    print("Your grade is D")
