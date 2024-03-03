from random import randint
random_numbers = [randint(1, 50) for _ in range(10)]
print(random_numbers)


def multiply_list_elements(g: list['int']):
    prd = 1
    for d in g:
        prd = prd * d
    return prd


print("Product of elements of list =", multiply_list_elements(random_numbers))
