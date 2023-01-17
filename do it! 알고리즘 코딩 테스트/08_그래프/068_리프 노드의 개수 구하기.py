import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(int(1e6))

n = int(input())
visited = [False] * n
tree = [[] for _ in range(n)]
answer = 0
p = list(map(int, input().split()))

for i in range(n):
    if p[i] != -1:
        tree[i].append(p[i])
        tree[p[i]].append(i)
    else:
        root = i

def dfs(number):
    global answer
    visited[number] = True
    cNode = 0
    for i in tree[number]:
        if not visited[i] and i != deleteNode:
            cNode += 1
            dfs(i)
    if cNode == 0:
        answer += 1

deleteNode = int(input())

if deleteNode == root:
    print(0)
else:
    dfs(root)
    print(answer)