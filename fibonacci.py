limit = int(input("Enter the limit:"))
fibonacci_sequence = [1, 1]
for x in range(limit):
    temp = fibonacci_sequence[x] + fibonacci_sequence[x + 1]
    fibonacci_sequence.append(temp)
    print(fibonacci_sequence)
