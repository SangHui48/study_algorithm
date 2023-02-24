from collections import deque

def solution(info, edges):
    answer = []
    graph = [[] for _ in range(len(info) + 1)]
    visit = [False] * (len(info) + 1)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    q = deque((edges[0][0], edges[0][1], [info[0]]))
    while q:
        now = q.popleft()

    return answer
