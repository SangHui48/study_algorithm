import sys
input = lambda : sys.stdin.readline()
n, m = map(int, input().split())
edges = []
distance = [sys.maxsize] * (n + 1)

for _ in range(m):
    edges.append(tuple(map(int, input().split())))

distance[1] = 0

for _ in range(n - 1):
    for start, end, time in edges:
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
            distance[end] = distance[start] + time

cycle = False

for start, end, time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
        cycle = True

if not cycle:
    for i in range(2, n+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)