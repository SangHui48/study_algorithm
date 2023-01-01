import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [[sys.maxsize] * k for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

pq = [(0, 1)]
distance[1][0] = 0

while pq:
    cost, node = heapq.heappop(pq)
    for next_node, next_cost in graph[node]:
        temp = cost + next_cost
        if distance[next_node][k-1] > temp:
            distance[next_node][k-1] = temp
            distance[next_node].sort()
            heapq.heappush(pq, (temp, next_node))

for i in range(1, n+1):
    if distance[i][k-1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][k-1])