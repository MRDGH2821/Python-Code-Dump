sum = 0
a = int(input("Enter number to find sum of digits: "))
while a > 0:
    sum = sum + int(a % 10)
    a = a // 10
print("Sum is", sum)
