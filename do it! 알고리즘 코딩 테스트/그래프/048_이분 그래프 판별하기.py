import sys
sys.setrecursionlimit(10**6)
input = lambda : sys.stdin.readline().rstrip()
k = int(input())

def dfs(node):
    global isEven
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            check[i] = (check[node] + 1) % 2
            dfs(i)
        elif check[node] == check[i]:
            isEven = False

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (v + 1)
    check = [0] * (v + 1)
    isEven=True
    for i in range(1, v+1):
        if isEven:
            dfs(i)
        else:
            break

    if isEven:
        print('YES')
    else:
        print('NO')