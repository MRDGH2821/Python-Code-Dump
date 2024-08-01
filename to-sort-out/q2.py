in_list1 = [int(x) for x in input().split()]
in_list2 = [int(x) for x in input().split()]


def check(in_list1, in_list2):
    sum1 = sum(in_list1)
    sum2 = sum(in_list2)
    pairs = list()
    if sum1 == sum2:
        print(-1)
    else:
        for i in range(len(in_list1)):
            for j in range(len(in_list2)):
                temp = in_list1[i]
                in_list1[i] = in_list2[j]
                in_list2[j] = temp

                sum1 = sum(in_list1)
                sum2 = sum(in_list2)
                if (sum1 == sum2):
                    if (sum1 % 2 == 0):
                        pairs.append(
                            tuple([in_list2[j], in_list1[i], "evens"]))
                    else:
                        pairs.append(tuple([in_list2[j], in_list1[i], "odds"]))
                    temp = in_list1[i]
                    in_list1[i] = in_list2[j]
                    in_list2[j] = temp
                else:
                    temp = in_list1[i]
                    in_list1[i] = in_list2[j]
                    in_list2[j] = temp
    return pairs


def product(pairs):
    odd_list = list()
    even_list = list()
    for pair in pairs:

        return products
