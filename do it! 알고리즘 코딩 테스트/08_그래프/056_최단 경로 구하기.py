import sys
from queue import PriorityQueue
input = lambda : sys.stdin.readline().rstrip()

V, E = map(int, input().split())
k = int(input())
distance = [sys.maxsize] * (V + 1)
visited = [False] * (V + 1)
graph = [[] for _ in range(V + 1)]
q = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

q.put((0, k))
distance[k] = 0

while q.qsize() > 0:
    now = q.get()
    currnet_node = now[1]
    if visited[currnet_node]:
        continue
    visited[currnet_node] = True
    for next in graph[currnet_node]:
        next_node = next[0]
        weight = next[1]
        if distance[next_node] > distance[currnet_node] + weight:
            distance[next_node] = distance[currnet_node] + weight
            q.put((distance[next_node], next_node))

for i in range(1, V+1):
    if visited[i]:
        print(distance[i])
    else:
        print('INF')