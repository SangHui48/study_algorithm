import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()
print = sys.stdout.write

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

depth = [0] * (n + 1)
visited = [False] * (n + 1)
temp = 1
kmax = 0

while temp <= n:
    temp <<= 1
    kmax += 1

parent = [[0 for _ in range(n + 1)] for _ in range(kmax + 1)]

def bfs(node):
    q = deque()
    q.append(node)
    visited[node] = True
    level = 1
    now_size = 1
    cnt = 0
    while q:
        now = q.popleft()
        for next in tree[now]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                parent[0][next] = now
                depth[next] = level
        cnt += 1
        if cnt == now_size:
            cnt = 0
            now_size = len(q)
            level += 1
bfs(1)

for k in range(1, kmax + 1):
    for n in range(1, n+1):
        parent[k][n] = parent[k-1][parent[k-1][n]]

def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    for k in range(kmax, -1, -1):
        if pow(2, k) <= depth[b] -depth[a]:
            if depth[a] <= depth[parent[k][b]]:
                b = parent[k][b]

    for k in range(kmax, -1, -1):
        if a == b:
            break
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    LCA = a
    if a != b:
        LCA = parent[0][LCA]
    return LCA

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(str(lca(a, b)))
    print('\n')