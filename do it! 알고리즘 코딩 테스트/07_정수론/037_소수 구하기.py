# 에라토스테네스의 체
import sys
input = lambda : sys.stdin.readline().rstrip()

m, n = map(int, input().split())
data = [0] * (n + 1)

for i in range(2, n+1):
    data[i] = i

for i in range(2, int())