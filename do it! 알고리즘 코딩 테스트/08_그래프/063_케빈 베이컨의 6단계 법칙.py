import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

minimum = sys.maxsize
answer = -1

for i in range(1, n + 1):
    temp = 0
    for j in range(1, n + 1):
        temp += graph[i][j]
    if minimum > temp:
        minimum = temp
        answer = i

print(answer)
