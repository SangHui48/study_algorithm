# https://www.acmicpc.net/problem/2098
import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
w = []

for i in range(n):
    w.append([])
    w[i] = list(map(int, input().split()))

dp = [[0 for j in range(1 << 16)] for i in range(16)]

def tsp(c, v):
    if v == (1 << n) - 1:
        if w[c][0] == 0:
            return float('inf')
        else:
            return w[c][0]
    if dp[c][v] != 0:
        return dp[c][v]
    
    min_val = float('inf')
    for i in range(0, n):
        if (v & (1 << i)) == 0 and w[c][i] != 0:
            min_val = min(min_val, tsp(i, (v | (1 << i))) + w[c][i])
    dp[c][v] = min_val
    return dp[c][v]

print(tsp(0, 1))