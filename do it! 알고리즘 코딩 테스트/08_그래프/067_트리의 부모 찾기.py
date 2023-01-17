import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(int(1e6))

n = int(input())
visited = [False] * (n + 1)
tree = [[] for _ in range(n + 1)]
answer = [0] * (n + 1)

for _ in range(1, n):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

def dfs(number):
    visited[number] = True
    for i in tree[number]:
        if not visited[i]:
            answer[i] = number
            dfs(i)

dfs(1)

for i in range(2, n+1):
    print(answer[i])