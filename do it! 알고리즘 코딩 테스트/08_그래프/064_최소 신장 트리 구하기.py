import sys
from queue import PriorityQueue
input = lambda : sys.stdin.readline().rstrip()

v, e = map(int, input().split())
pq = PriorityQueue()
parent = [0] * (v + 1)
for i in range(v + 1):
    parent[i] = i

for i in range(e):
    s, e, w = map(int, input().split())
    pq.put((w, s, e))

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

use_edge = 0
result = 0
while use_edge < v - 1:
    w, s, e = pq.get()
    if find(s) != find(e):
        union(s, e)
        result += w
        use_edge += 1

print(result)