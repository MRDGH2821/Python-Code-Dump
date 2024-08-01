from copy import deepcopy as copy
sticks = int(input())
capacity = int(input())
stick_length: "list[int]" = list()
for i in range(sticks):
    stick_length.append(int(input()))


def Box_Value(array: "list[int]"):
    sum = 0
    for i in array:
        sum = sum + (i**2)
    return sum


def breaks(capacity: int, stick_length: "list[int]"):
    new_stick_lengths = copy(stick_length)
    temp = Box_Value(stick_length)
    stick_b = 1
    stick_a = 0
    for one_stick in stick_length:
        stick_a = one_stick - stick_b
        new_stick_lengths.remove(one_stick)
        new_stick_lengths.append(stick_a)
        new_stick_lengths.append(stick_b)
        if len(new_stick_lengths) < capacity:
            box_val = Box_Value(new_stick_lengths)
            if temp > box_val:
                temp = box_val
            else:
                new_stick_lengths.remove(stick_a)
                new_stick_lengths.remove(stick_b)
                stick_b = stick_b + 1
