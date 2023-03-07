import sys
input = lambda : sys.stdin.readline().rstrip()
n, m = map(int, input().split())
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
answer = 0

for i in range(n):
    nums = list(input())
    for j in range(m):
        dp[i][j] = int(nums[j])
        if dp[i][j] == 1 and i > 0 and j > 0:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + dp[i][j]
        if answer < dp[i][j]:
            answer = dp[i][j]
print(answer ** 2)