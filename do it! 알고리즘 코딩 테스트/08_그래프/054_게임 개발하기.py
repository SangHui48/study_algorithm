import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
build_time = [0] * (n + 1)
for i in range(1, n+1):
    data = list(map(int, input().split()))
    build_time[i] = data[0]
    index = 1
    while True:
        pretemp = data[index]
        index += 1
        if pretemp == -1:
            break
        graph[pretemp].append(i)
        indegree[i] += 1

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

result = [0] * (n + 1)
while q:
    now = q.popleft()
    for next in graph[now]:
        indegree[next] -= 1
        result[next] = max(result[next], result[now] + build_time[now])
        if indegree[next] == 0:
            q.append(next)

for i in range(1, n+1):
    print(result[i] + build_time[i])