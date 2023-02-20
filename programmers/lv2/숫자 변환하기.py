# https://school.programmers.co.kr/learn/courses/30/lessons/154538
import sys
def solution(x, y, n):
    answer = 0
    dp = [sys.maxsize] * (y + 1)
    dp[x] = 0
    for i in range(x, y+1):
        dp[i] = min(dp[i-n] + 1, dp[i])
        if i % 2 == 0:
            dp[i] = min(dp[i // 2] + 1, dp[i])
        if i % 3 == 0:
            dp[i] = min(dp[i // 3] + 1, dp[i])
    return dp[y] if dp[y] != sys.maxsize else -1

print(solution(10, 40, 5))