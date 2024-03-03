def sq_list(j):
    squared_list = [g**2 for g in range(j + 1)]
    return squared_list


a = int(input("Input a number:"))
print(sq_list(a))
