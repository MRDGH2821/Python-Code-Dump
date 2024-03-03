def factors(n):
    for i in range(1, n + 1, 1):
        if n % i == 0:
            print(i)


a = int(input("Enter a number to get all factors: "))
factors(a)
