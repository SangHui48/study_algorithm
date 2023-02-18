import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
data = []
for _ in range(n):
    data.append(tuple(map(int, input().split())))
