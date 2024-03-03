from random import randint
random_numbers = [randint(1, 50) for _ in range(10)]
print(random_numbers)


def listmul(g):
    prd = 1
    for d in g:
        prd = prd * d
    return prd


print("Product of elements of list =", listmul(random_numbers))
