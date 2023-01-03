import sys
sys.setrecursionlimit(100000)
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
city = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n+1):
    city[i] = list(map(int, input().split()))
    city[i].insert(0, 0)
plan = list(map(int, input().split()))
plan.insert(0, 0)
parent = [i for i in range(n + 1)]

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

for i in range(1, n+1):
    for j in range(1, n + 1):
        if city[i][j] == 1:
            union(i, j)

index = find(plan[1])
isConnect = True
for i in range(2, len(plan)):
    if index != find(plan[i]):
        isConnect = False
        break

if isConnect:
    print('YES')
else:
    print('NO')