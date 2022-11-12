import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))
data.sort()
m = int(sys.stdin.readline().rstrip())
request = list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(data, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

for x in request:
    result = binary_search(data, x, 0, n - 1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end = ' ')