import sys
from collections import deque
read = lambda : sys.stdin.readline().rstrip()

n, m = map(int, read().split())
graph = []
visited = [[False] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, read())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))

bfs(0, 0)
print(graph[n-1][m-1])