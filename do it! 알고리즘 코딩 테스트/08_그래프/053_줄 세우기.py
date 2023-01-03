import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n + 1)

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    indegree[end] += 1

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    print(now, end=' ')
    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)