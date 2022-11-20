import sys
input = sys.stdin.readline

INF = int(1e9) # 무한을 의마하는 값으로 10억 설정
n, m = map(int, input().split()) # 노드의 개수 및 간선 입력
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는것은 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

# 각 간선의 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 K 입력받기
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = graph[1][k] + graph[k][x]

if answer >= INF:
    print(-1)
else:
    print(answer)