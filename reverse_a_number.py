"""
Number reverse
"""
a = int(input("Enter number: "))
rev = 0
while a > 0:
    rev = 10 * rev + a % 10
    a = a // 10
print("Reverse: ", rev)
