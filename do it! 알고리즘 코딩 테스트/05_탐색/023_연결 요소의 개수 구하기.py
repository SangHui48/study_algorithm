import sys
sys.setrecursionlimit(10000)
read = lambda : sys.stdin.readline().rstrip()

n, m = map(int, read().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

for _ in range(m):
    u, v = map(int, read().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0

for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)

