import sys
from collections import deque
from queue import PriorityQueue

input = lambda : sys.stdin.readline().rstrip()
n, m = map(int, input().split())
visited = [[False for _ in range(m)] for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

sNum = 1 # 섬 번호
sumlist = list([]) # 모든 섬 정보 이중 리스트
mlist = [] # 1개의 섬 정보 리스트

def addNode(i, j, queue):
    graph[i][j] = sNum
    visited[i][j] = True
    temp = [i, j]
    mlist.append(temp)
    queue.append(temp)

def bfs(i, j):
    queue = deque()
    mlist.clear()
    start = [i, j]
    queue.append(start)
    mlist.append(start)
    visited[i][j] = True
    graph[i][j] = sNum

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = 