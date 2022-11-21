import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
data = [0] * (n + 1)
for i in range(1, n + 1):
    data[i] = int(input())
