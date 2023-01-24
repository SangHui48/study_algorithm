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
parent = [0] * (n + 1)
visited = [False] * (n + 1)

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
                parent[next] = now
                depth[next] = level
        cnt += 1
        if cnt == now_size: # 현재 뎁스 탐색 종료되면,
            cnt = 0
            now_size = len(q) # 바로 아래 뎁스 노드 개수로 갱신해주기
            level += 1

bfs(1)

def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a

    while depth[a] != depth[b]:
        a = parent[a]
    while a != b:
        a = parent[a]
        b = parent[b]

    return a

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(str(lca(a, b)))
    print('\n')