import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    s, e, v = map(int, input().split())
    graph[s].append((e, v))
    reverse_graph[e].append((s, v))
    indegree[e] += 1

start, end = map(int, input().split())

q = deque()
q.append(start)
result = [0] * (n + 1)

while q:
    now = q.popleft()
    for next in graph[now]:
        indegree[next[0]] -= 1
        result[next[0]] = max(result[next[0]], result[now] + next[1])
        if indegree[next[0]] == 0:
            q.append(next[0])

result_cnt = 0
visited = [False] * (n + 1)
q.clear()
q.append(end)
visited[end] = True

while q:
    now = q.popleft()
    for next in reverse_graph[now]:
        if result[next[0]] + next[1] == result[now]:
            result_cnt += 1
            if not visited[next[0]]:
                visited[next[0]] = True
                q.append(next[0])

print(result[end])
print(result_cnt)