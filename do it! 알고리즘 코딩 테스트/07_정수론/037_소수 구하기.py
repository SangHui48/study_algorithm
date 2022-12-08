# 에라토스테네스의 체
import sys
import math
input = lambda : sys.stdin.readline().rstrip()

m, n = map(int, input().split())
data = [0] * (n + 1)

for i in range(2, n+1):
    data[i] = i

for i in range(2, int(math.sqrt(n)) + 1):
    if data[i] == 0:
        continue
    for j in range(i + i, n + 1, i):
        data[j] = 0

for i in range(m, n + 1):
    if data[i] != 0:
        print(data[i])