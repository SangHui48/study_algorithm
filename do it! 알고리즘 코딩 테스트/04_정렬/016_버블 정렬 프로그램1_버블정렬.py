import sys
input = sys.stdin.readline

n = int(input())
data = []
for i in range(n):
    data.append((int(input()), i))

answer = 0
data.sort()

for i in range(n):
    if data[i][1] - i > answer:
        answer = data[i][1] - i

print(answer + 1)

