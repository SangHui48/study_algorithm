import sys
from queue import PriorityQueue

input = lambda : sys.stdin.readline().rstrip()
n = int(input())
pq = PriorityQueue()
total = 0

for i in range(n):
    tempC = list(input())
    for j in range(n):
        temp = 0
        if 'a' <= tempC[j] <= 'z':
            temp = ord(tempC[j]) - ord('a') + 1
        elif 'A' <= tempC[j] <= 'Z':
            temp = ord(tempC[j]) - ord('A') + 27
        total += temp
        if i != j and temp != 0:
            pq.put((temp, i, j))

parent = [i for i in range(n)]

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

useEdge = 0
result = 0

while pq.qsize() > 0:
    v, s, e = pq.get()
    if find(s) != find(e):
        union(s, e)
        result += v
        useEdge += 1

if useEdge == n-1:
    print(total - result)
else:
    print(-1)