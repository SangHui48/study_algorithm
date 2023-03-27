# https://www.acmicpc.net/problem/11049
import sys
sys.setrecursionlimit(100000)
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
m = []
dp = [[-1 for j in range(n + 1)] for i in range(n + 1)]
m.append((0, 0))

for _ in range(n):
    m.append(tuple(map(int, input().split())))

def execute(s, e):
    result = sys.maxsize
    if dp[s][e] != -1:
        return dp[s][e]
    if s == e:
        return 0
    if s + 1 == e:
        return m[s][0] * m[s][1] * m[e][1]
    for i in range(s, e):
        result = min(result, m[s][0] * m[i][1] * m[e][1] + execute(s, i) + execute(i+1, e))
    dp[s][e] = result
    return dp[s][e]

print(execute(1, n))