import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
parent = [0] * (n + 1)

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

def checkSame(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for i in range(n+1):
    parent[i] = i

for _ in range(m):
    query, a, b = map(int, input().split())
    if query == 0:
        union(a, b)
    elif query == 1:
        if checkSame(a, b):
            print('YES')
        else:
            print('NO')