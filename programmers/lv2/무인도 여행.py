# https://school.programmers.co.kr/learn/courses/30/lessons/154540
import sys
sys.setrecursionlimit(int(1e7))
def solution(maps):
    answer = []
    n = len(maps)  # row
    m = len(maps[0])  # col
    visited = [[False] * m for _ in range(n)]

    def dfs(i, j, visited):
        if 0<= i < n and 0 <= j < m:
            if not visited[i][j] and maps[i][j] != 'X':
                visited[i][j] = True
                L = dfs(i, j-1, visited)
                R = dfs(i, j+1, visited)
                U = dfs(i+1, j, visited)
                D = dfs(i-1, j, visited)
                return int(maps[i][j]) + L + R + U + D
            else:
                return 0
        else:
            return 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != 'X':
                tmp = dfs(i, j, visited)
                if tmp > 0:
                    answer.append(tmp)
    if answer:
        answer.sort()
        return answer
    else:
        return [-1]
