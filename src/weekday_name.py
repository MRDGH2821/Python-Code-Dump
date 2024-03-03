day = int(input("Enter no. of day:"))
if (day == 1) or (day % 7 == 1):
    print("Monday")
elif (day == 2) or (day % 7 == 2):
    print("Tuesday")
elif (day == 3) or (day % 7 == 3):
    print("Wednesday")
elif (day == 4) or (day % 7 == 4):
    print("Thursday")
elif (day == 5) or (day % 7 == 5):
    print("Friday")
elif (day == 6) or (day % 7 == 6):
    print("Saturday")
elif (day == 7) or (day % 7 == 7):
    print("Sunday")
else:
    print("Invalid Number")
