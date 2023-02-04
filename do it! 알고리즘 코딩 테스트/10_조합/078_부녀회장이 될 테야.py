import sys
input = lambda : sys.stdin.readline().rstrip()
dp = [[0 for _ in range(15)] for _ in range(15)]
for i in range(1, 15):
    dp[i][1] = 1
    dp[0][i] = i

for i in range(1, 15):
    for j in range(2, 15):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(dp[k][n])