import sys
read = lambda : sys.stdin.readline().rstrip()

n = int(read())
data = list(map(int, read().split()))
data.sort()
m = int(read())
targets = list(map(int, read().split()))

for target in targets:
    start = 0
    end = len(data) - 1
    find = False

    while start <= end:
        mid = (start + end) // 2
        if data[mid] > target:
            end = mid - 1
        elif data[mid] < target:
            start = mid + 1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)
