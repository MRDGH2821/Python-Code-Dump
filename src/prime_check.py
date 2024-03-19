"""Prime number checker."""

number = int(input("Enter a number: "))
flag = 1
for x in range(2, number):
    if number % x == 0:
        flag = 1
        break
    else:
        flag = 0
if flag == 0:
    print(number, "is prime")
else:
    print(number, "is not prime")
