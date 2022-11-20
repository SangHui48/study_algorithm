import sys
input = sys.stdin.readline

INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

# 노드의 개수 및 간선의 개수 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에게 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    graph[a][a] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우 INFINITY라고 출력
        if graph[a][b] == INF:
            print('INFINITY', end=' ')
        else:
            print(graph[a][b], end=' ')
    print()