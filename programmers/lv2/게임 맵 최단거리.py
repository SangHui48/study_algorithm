# https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visit = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if maps[ny][nx] != 0 and not visit[ny][nx]:
                    maps[ny][nx] = maps[y][x] + 1
                    visit[ny][nx] = True
                    q.append((nx, ny))
    if maps[n - 1][m - 1] != 1:
        return maps[n - 1][m - 1]
    else:
        return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))