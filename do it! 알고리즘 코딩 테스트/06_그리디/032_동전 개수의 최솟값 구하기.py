import sys
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

answer = 0
for i in range(len(data)-1, -1, -1):
    if k // data[i] != 0:
        answer += (k // data[i])
        k = k % data[i]

print(answer)