import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

answer = []
visited = [-1] * (n + 1)
visited[x] = 0
def bfs(v):
    q = deque()
    q.append(v)
    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if visited[next_node] == -1:
                visited[next_node] = visited[now] + 1
                q.append(next_node)

bfs(x)
check = False
for i in range(1, n+1):
    if visited[i] == k:
        print(i)
        check = True

if not check:
    print(-1)
