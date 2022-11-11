import sys
n, m = map(int, sys.stdin.readline().split())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

idx_info = []
for _ in range(m):
    idx_info.append(tuple(map(int, sys.stdin.readline().split())))

sum_info = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        sum_info[i][j] = sum_info[i][j-1] + sum_info[i-1][j] - sum_info[i-1][j-1] + data[i-1][j-1]

for x1, y1, x2, y2 in idx_info:
    print(sum_info[x2][y2] - sum_info[x1-1][y2] - sum_info[x2][y1-1] + sum_info[x1-1][y1-1])