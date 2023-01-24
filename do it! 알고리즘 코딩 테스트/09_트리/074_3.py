# 1, 2, 4, 8, ... 칸씩 건너뛰면서 조상노드를 탐색 (시간복잡도 이점)
# 동빈나 --> https://www.youtube.com/watch?v=O895NbxirM8
# 내코드 --> http://boj.kr/ffae1d979e1646bebc1ba01b2ffdf9cc

import sys
sys.setrecursionlimit(10 ** 6)
si = sys.stdin.readline


def dfs(x, d):
  for y in graph[x]:
    if p[y] < 0:
      p[y] = x
      depth[y] = d + 1
      dfs(y, d + 1)


def lca(a, b):
  # b가 더 깊도록 설정
  if depth[a] > depth[b]:
    a, b = b, a

  while depth[a] != depth[b]:
    b = p[b]

  while a != b:
    a = p[a]
    b = p[b]

  return a


if __name__ == "__main__":
  n = int(si())

  graph = [[] for _ in range(n + 1)]  # 양방향 인접리스트
  for _ in range(n - 1):
    a, b = map(int, si().split())
    graph[a].append(b)
    graph[b].append(a)

  p = [-1] * (n + 1)
  depth = [0] * (n + 1)

  p[1] = 0
  dfs(1, 0)

  # 공통 조상 탐색
  cache = dict()
  m = int(si())

  for _ in range(m):
    a, b = map(int, si().split())

    if (a, b) in cache:
      print(cache[(a, b)])
    else:
      cache[(a, b)] = cache[(b, a)] = lca(a, b)
      print(cache[(a, b)])