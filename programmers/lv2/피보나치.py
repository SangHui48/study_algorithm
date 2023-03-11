# https://school.programmers.co.kr/learn/courses/30/lessons/12945
def solution(n):
    dp = [0]*1000001
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    answer = dp[n]
    return answer