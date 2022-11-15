import sys
from collections import deque
read = sys.stdin.readline

n, l = map(int, read().rstrip().split())
q = deque()
data = list(map(int, read().rstrip().split()))

for i in range(n):
    while q and q[-1][1] > data[i]: # 큐 마지막 위치에서 현제값보다 큰 수 제거
        q.pop()
    q.append((i, data[i])) # 큐 마지막에 현재값 저장
    if q[0][0] <= i - l: # 슬라이딩 윈도우 값을 벗어나면 제거
        q.popleft()
    print(q[0][1], end=' ')