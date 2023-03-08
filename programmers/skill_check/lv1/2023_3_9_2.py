def solution(board, moves):
    answer = 0
    stack = []

    def check(command):
        for i in range(len(board)):
            if board[i][command - 1] != 0:
                value = board[i][command - 1]
                board[i][command - 1] = 0
                return value
        return 0

    for command in moves:
        now = check(command)
        if now != 0:
            stack.append(now)
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2


    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))