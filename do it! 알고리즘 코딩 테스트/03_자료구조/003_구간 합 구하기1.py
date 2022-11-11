import sys
n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
idx_info = []
for _ in range(m):
    idx_info.append(tuple(map(int, sys.stdin.readline().split())))

tmp = 0
sum_info = [0] * (n + 1)
for i in range(1, len(data) + 1):
    tmp += data[i-1]
    sum_info[i] = tmp

for start, end in idx_info:
    print(sum_info[end] - sum_info[start-1])