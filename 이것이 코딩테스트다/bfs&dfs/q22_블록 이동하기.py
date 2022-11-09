from collections import deque

def get_next_pos(pos, board):
    pass

def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)] # 로봇이 벽을 벗어나는지 더 간단하게 관찰하기 위해서
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)} # 로봇 초기 위치
    q.append((pos, 0))
    visited.append(pos)
    while q:
        pos, cost = q.popleft()
        if (n, n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            pass
