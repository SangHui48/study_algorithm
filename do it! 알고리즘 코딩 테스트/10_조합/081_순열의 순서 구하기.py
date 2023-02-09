# https://www.acmicpc.net/problem/1722

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
data = list(map(int, input().split()))
visited = [False] * (n + 1)
for i in range(1, n + 1):
    dp[i] = dp[i-1] * i
if data[0] == 1:
    answer = [0] * (n + 1)
    k = data[1]
    for i in range(1, n+1):
        cnt = 1
        for j in range(1, n + 1):
            if visited[j]:
                continue
            if k <= cnt * dp[n-i]:
                x = dp[n-i]
                k -= (cnt - 1) * dp[n-i]
                answer[i] = j
                visited[j] = True
                break
            cnt += 1
    for i in range(1, n + 1):
        print(answer[i], end=' ')
elif data[0] == 2:
    k = 1
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, data[i]):
            if not visited[j]:
                cnt += 1
        k += cnt * dp[n-i]
        visited[data[i]] = True
    print(k)