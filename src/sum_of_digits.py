"""Sum of digits."""

digit_sum = 0
a = int(input("Enter number to find sum of digits: "))
while a > 0:
    digit_sum = digit_sum + int(a % 10)
    a = a // 10
print("Sum is", digit_sum)
