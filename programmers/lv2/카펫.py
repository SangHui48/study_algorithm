#https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    answer = []
    for h in range(1, yellow + 1):
        if yellow % h == 0:
            w = yellow // h
            if (w * 2) + 2 * (h + 2) == brown:
                answer += [w + 2, h + 2]
                break
    return answer