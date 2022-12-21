n = int(input())
graph = [[] for _ in range(n)]
visited = [False] * n
d = [0] * n # 각 노드값 저장 리스트
lcm = 1 # 최소공배수

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def dfs(v):
    visited[v] = True
    for node, p, q in graph[v]:
        next = node
        if not visited[next]:
            d[next] = d[v] * q // p
            dfs(next)

for _ in range(n-1):
    a, b, p, q = map(int, input().split())
    graph[a].append((b, p, q))
    graph[b].append((a, q, p))
    lcm *= (p * q // gcd(p, q))

d[0] = lcm
dfs(0)
mgcd = d[0]

for i in range(1, n):
    mgcd = gcd(mgcd, d[i])

for i in range(n):
    print(d[i]//mgcd, end=' ')