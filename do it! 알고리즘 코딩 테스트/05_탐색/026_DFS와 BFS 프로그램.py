import sys
from collections import deque
sys.setrecursionlimit(10000)
read = lambda : sys.stdin.readline().rstrip()

n, m, v = map(int, read().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end = map(int, read().split())
    graph[start].append(end)
    graph[end].append(start)

# 노드가 같을 경우 번호가 작은 노드 부터 방문한다 했으므로
for i in range(n + 1):
    graph[i].sort()

def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
visited = [False] * (n + 1)
dfs(v)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

print()
visited = [False] * (n + 1)
bfs(v)
