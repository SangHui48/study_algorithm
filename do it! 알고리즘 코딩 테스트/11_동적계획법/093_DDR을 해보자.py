# https://www.acmicpc.net/problem/2342
import sys
input = lambda : sys.stdin.readline().rstrip()

dp = [[[sys.maxsize for k in range(5)] for j in range(5)] for i in range(100001)]
mp = [[0, 2, 2, 2, 2],
      [2, 1, 3, 4, 3],
      [2, 3, 1, 3, 4],
      [2, 4, 3, 1, 3],
      [2, 3, 4, 3, 1]]

s = 1
dp[0][0][0] = 0

inputList = list(map(int, input().split()))
index = 0

while inputList[index] != 0:
    n = inputList[index]
    for i in range(5):
        if n == i:
            continue
        for j in range(5):
            dp[s][i][n] = min(dp[s-1][i][j] + mp[j][n], dp[s][i][n])
    
    for j in range(5):
        if n == j:
            continue
        for i in range(5):
            dp[s][n][j] = min(dp[s-1][i][j] + mp[i][n], dp[s][n][j])

    s += 1
    index += 1

s -= 1
result = sys.maxsize

for i in range(5):
    for j in range(5):
        result = min(result, dp[s][i][j])
print(result)