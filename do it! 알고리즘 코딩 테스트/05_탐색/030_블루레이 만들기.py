import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
data = list(map(int, input().split()))

start = max(data)
end = sum(data)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    count = 0
    for i in range(n):
        if sum + data[i] > mid:
            count += 1
            sum = 0
        sum += data[i]

    if sum != 0:
        count += 1
    if count > m:
        start = mid + 1
    else:
        end = mid - 1

print(start)