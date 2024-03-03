a = int(input("Enter a number:"))
b = a
flag = 0
for x in range(2, b):
    if a % x == 0:
        flag = 1
        break
    else:
        flag = 0
if flag == 0:
    print(b, "is prime")
else:
    print(b, "is not prime")
