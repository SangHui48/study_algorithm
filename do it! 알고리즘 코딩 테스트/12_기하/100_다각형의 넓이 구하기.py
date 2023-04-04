# https://www.acmicpc.net/problem/2166
import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
x, y = [], []

for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.append(x[0])
y.append(y[0])

result = 0
for i in range(n):
    result += (x[i]*y[i+1]) - (x[i+1]*y[i])
print(round(abs(result/2), 1)) 