# https://school.programmers.co.kr/learn/courses/30/lessons/17679
# 직접 보드를 조작하기 보단 지워지는 블록들의 인덱스를 기억해두면 편했을 것
# def solution(m, n, board):
#     answer = 0
#     def check(i, j):
#         dx = [-1, 1, 0, 0]
#         dy = [0, 0, -1, 1]
#         for i in range(4):
#             nx = i + dx[i]
#             ny = j + dy[i]
#             if 0 <= nx < m and 0 <= ny < n:
#                 if board[nx][ny] == 0 or board[i][j] != board[nx][ny]:
#                     return False
#         return True
    
#     def move_element(board):
#         for i in range(m):
#             for j in range(n):
#                 if i == m - 1:
#                     pass
#                 else:
#                     if board[i][j] == 0 and board[i+1][j] != 0:
#                         board
#     return answer

def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
    answer = 0
    rm = set()
    while True:
        for i in range(m-1):
            for j in range(n-1):
                check = board[i][j]
                if board[i][j] == "":
                    continue
                if board[i+1][j] == check and board[i][j+1] == check and board[i+1][j+1] == check:
                    rm.add((i, j))
                    rm.add((i, j+1))
                    rm.add((i+1, j))
                    rm.add((i+1, j+1))
        if rm:
            answer += len(rm)
            for i, j in rm:
                board[i][j] = ""
            rm = set()
        else:
            return answer
        
        while True:
            flag = False
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j] == "":
                        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                        flag = True
                        
            if not flag:
                break