import sys
sys.setrecursionlimit(10000)
read = lambda: sys.stdin.readline().rstrip()

n, m = map(int, read().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

arrive = False

def dfs(now, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visited[now] = True
    for i in graph[now]:
        if not visited[i]:
            dfs(i, depth + 1)
    visited[now] = False

for _ in range(m):
    start, end = map(int, read().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(n):
    dfs(i, 1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)