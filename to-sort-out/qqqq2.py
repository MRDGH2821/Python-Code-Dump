def performOperations(arr, operations):

    for i in operations:
        x = i[0]
        y = i[1]
        arr = list()
        temp = arr[x:y + 1]
        temp = temp[::-1]
        for j in range(x, y + 1):
            arr[j] = temp[j - x]
    return arr


arr_count = int(input().strip())

arr = list()
for _ in range(arr_count):
    arr_item = int(input().strip())
    arr.append(arr_item)

rows = int(input().strip())
column = int(input().strip())
operations = list()
for _ in range(rows):
    operations.append(list(map(int, input().rstrip().split())))
result = performOperations(arr, operations)
print('\n'.join(map(str, result)))
