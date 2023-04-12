# https://school.programmers.co.kr/learn/courses/30/lessons/12924
def solution(n):
    answer = 0
    for i in range(1, n+1):
        total = 0
        for j in range(i, n+1):
            total += j
            if total == n:
                answer += 1
            elif total > n:
                break
    return answer