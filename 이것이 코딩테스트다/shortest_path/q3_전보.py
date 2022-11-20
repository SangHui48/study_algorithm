import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]
# 최단 거리 테이블
distance = [INF] * (n+1)

# 모든 간선에 대한 정보 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0 #시작점은 0으로 초기화
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

cnt = 0 #도달할 수 있는 노드의 개수
max_distance = 0 # 도달할 수 있는 노드중에서, 가장 멀리 있는 노드와의 최단거리

for d in distance:
    if d != INF:
        cnt += 1
        max_distance = max(max_distance, d)

print(cnt-1, max_distance)