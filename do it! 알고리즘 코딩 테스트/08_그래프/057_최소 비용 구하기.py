import sys
from queue import PriorityQueue
input = lambda : sys.stdin.readline()

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
dist = [sys.maxsize] * (n + 1)
visited = [False] * (n + 1)

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

start, end = map(int, input().split())
q = PriorityQueue()
q.put((0, start))
dist[start] = 0
while q.qsize() > 0:
    now = q.get()
    current_node = now[1]
    if not visited[current_node]:
        visited[current_node] = True
        for next in graph[current_node]:
            if not visited[next[0]] and dist[next[0]] > dist[current_node] + next[1]:
                dist[next[0]] = dist[current_node] + next[1]
                q.put((dist[next[0]], next[0]))

print(dist[end])