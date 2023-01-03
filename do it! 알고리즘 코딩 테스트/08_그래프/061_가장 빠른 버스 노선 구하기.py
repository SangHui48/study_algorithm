import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
graph = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n+1):
    graph[i][i] = 0

for i in range(m):
    s, e, v = map(int, input().split())
    if graph[s][e] > v:
        graph[s][e] = v

for k in range(1, n+1):
    for i in range(1, n + 1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == sys.maxsize:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
