# https://school.programmers.co.kr/learn/courses/30/lessons/132266
from collections import deque
def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]
    visit = [-1] * (n + 1)
    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)
    visit[destination] = 0
    q = deque([destination])
    while q:
        now = q.popleft()
        for next in graph[now]:
            if visit[next] == -1:
                visit[next] = visit[now] + 1
                q.append(next)
    return [visit[i] for i in sources]

print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))