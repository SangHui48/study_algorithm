import copy
import sys
from collections import deque
from queue import PriorityQueue
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
myMap = []
visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(n):
    myMap.append(list(map(int, input().split())))

sNum = 1 # 섬 번호
sumlist = list([]) # 모든 섬 정보 이중 리스트
mlist = [] # 1개의 섬 정보 리스트

def addNode(i, j, queue):
    myMap[i][j] = sNum
    visited[i][j] = True
    temp = [i, j]
    mlist.append(temp)
    queue.append(temp)

def bfs(i, j):
    q = deque()
    mlist.clear()
    start = [i, j]
    q.append(start)
    mlist.append(start)
    visited[i][j] = True
    myMap[i][j] = sNum

    while q:
        x, y = q.popleft()
        for i in range(4):
            tempR = dx[i]
            tempC = dy[i]
            while 0 <= x + tempR < n and 0 <= y + tempC < m:
                if not visited[x + tempR][y + tempC] and myMap[x + tempR][y + tempC] != 0:
                    addNode(x + tempR, y + tempC, q)
                else:
                    break
                if tempR < 0:
                    tempR -= 1
                elif tempR > 0:
                    tempR += 1
                elif tempC < 0:
                    tempC -= 1
                elif tempC > 0:
                    tempC += 1
    return mlist

for i in range(n):
    for j in range(m):
        if myMap[i][j] != 0 and not visited[i][j]:
            tempList = copy.deepcopy(bfs(i, j)) # 깊은 복사로 해야 주소 공유를 안함???
            sNum += 1
            sumlist.append(tempList)

pq = PriorityQueue()

for now in sumlist:
    for temp in now:
        x = temp[0] # row
        y = temp[1] # col
        now_S = myMap[x][y]
        for i in range(4):
            tempR = dx[i]
            tempC = dy[i]
            blength = 0
            while 0 <= x + tempR < n and 0 <= y + tempC < m:
                # 같은 섬이면 에지를 만들수 없음
                if myMap[x + tempR][y + tempC] == now_S:
                    break
                # 같은 섬도 아니고 바다도 아니면
                elif myMap[x + tempR][y + tempC] != 0:
                    if blength > 1: # 다른섬 -> 길이가 1이상일 때 에지로 더하기
                        pq.put((blength, now_S, myMap[x+tempR][y+tempC]))
                    break
                else: # 바다면 다리 길이 연장
                    blength += 1
                if tempR < 0:
                    tempR -= 1
                elif tempR > 0:
                    tempR += 1
                elif tempC < 0:
                    tempC -= 1
                elif tempC > 0:
                    tempC += 1

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

parent = [i for i in range(sNum)]
useEdge = 0
result = 0

while pq.qsize() > 0:
    v, s, e = pq.get()
    if find(s) != find(e):
        union(s, e)
        result += v
        useEdge += 1

if useEdge == sNum - 2:
    print(result)
else:
    print(-1)