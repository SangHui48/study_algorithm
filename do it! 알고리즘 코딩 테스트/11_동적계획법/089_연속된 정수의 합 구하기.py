# https://www.acmicpc.net/problem/13398
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
data = list(map(int, input().split()))
dp_l = [0] * n
dp_l[0] = data[0]
result = dp_l[0]
for i in range(1, n):
    dp_l[i] = max(data[i], dp_l[i-1] + data[i])
    result = max(result, dp_l[i])

dp_r = [0] * n
dp_r[n-1] = data[-1]
for i in range(n-2, -1, -1):
    dp_r[i] = max(data[i], dp_r[i+1] + data[i])

for i in range(1, n-1):
    result = max(result, dp_l[i-1] + dp_r[i+1])

print(result)