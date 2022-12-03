from collections import deque
import sys

read = lambda : sys.stdin.readline().rstrip()

n = int(read())
graph = [[] for _ in range(n + 1)]

for _ in range(n):
    data = list(map(int, read().split()))
    for i in range(1, len(data)-2, 2):
        graph[data[0]].append((data[i], data[i+1]))

distance = [0] * (n + 1)
visited = [False] * (n + 1)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i[0]]:
                visited[i[0]] = True
                q.append(i[0])
                distance[i[0]] += distance[now] + i[1]

bfs(1)
max_node = 1
for i in range(2, n+1):
    if distance[max_node] < distance[i]:
        max_node = i

distance = [0] * (n + 1)
visited = [False] * (n + 1)
bfs(max_node)
print(max(distance))