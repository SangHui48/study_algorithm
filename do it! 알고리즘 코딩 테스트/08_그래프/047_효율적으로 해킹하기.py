import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

answer = [0] * (n + 1)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = True
                answer[next_node] += 1
                q.append(next_node)

for i in range(1, n+1):
    visited = [False] * (n + 1)
    bfs(i)

max_val = max(answer)

for i in range(1, n+1):
    if answer[i] == max_val:
        print(i, end=' ')