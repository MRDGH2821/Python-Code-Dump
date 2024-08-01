scheduleStart = list()
scheduleEnd = list()


def maxPresentations(scheduleStart, scheduleEnd):
    # Write your code here
    sl = sorted((list(zip(*[scheduleStart, scheduleEnd]))), key=lambda x: x[1])
    sl = list(zip(*sl))
    lim = sl[1][0]
    n = 1
    for i in range(1, len(scheduleEnd)):
        if sl[0][i] >= lim:
            n = n + 1
            lim = sl[1][i]
    return n


schedule_count = int(input().strip())
print("Start times:\n")
for _ in range(schedule_count):
    item = int(input().strip())
    scheduleStart.append(item)
print("End times:\n")
for _ in range(schedule_count):
    item = int(input().strip())
    scheduleEnd.append(item)
result = maxPresentations(scheduleStart, scheduleEnd)
print(result)
