from collections import deque

def search(src, sign):
    return deque([(src, dest) for dest, check in enumerate(sign) if check])

def solution(n, signs):
    answer = [[0] * n for _ in range(n)]
    
    for start, sign in enumerate(signs):
        q = search(start, sign)

        while q:
            src, dest = q.popleft()

            if answer[src][dest] == 0:
                q += search(start, signs[dest])
                answer[src][dest] = 1

    return answer


print(solution(3, [[0,1,0],[0,0,1],[1,0,0]]))