# https://school.programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    if sum(d) <= budget:
        return len(d)
    answer = 0
    d.sort()
    for i in range(len(d)):
        if budget - d[i] < 0:
            break
        budget -= d[i]
        answer += 1
    return answer