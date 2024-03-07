numbers = [5, 7, 22, 97, 54, 62, 577, 623, 973, 661]
# numbers = [str(i)[::-1] for i in numbers].sort()
# print(numbers.sort(key=lambda x: x % 10, reverse=False))
# print(list(map(lambda x: x % 10, numbers)).sort())
print([i for i in numbers if i == i % 10].sort())
