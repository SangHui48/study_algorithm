# https://osnim.tistory.com/m/entry/%EB%B0%B1%EC%A4%80-14501-%ED%87%B4%EC%82%AC-Python

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
dp = [0] * (n + 2)
t = [0] * (n + 2)
p = [0] * (n + 2)

for i in range(1, n+1):
    t[i], p[i] = map(int, input().split())

for i in range(n, 0, -1):
    if i + t[i] > n+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i + t[i]] + p[i])

print(dp[1])