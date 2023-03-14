# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# from collections import Counter
# def solution(participant, completion):
#     print(Counter(participant))
#
# print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

def solution(participant, completion):
    d = {}
    for x in participant:
        d[x] = d.get(x, 0) + 1
    for x in completion:
        d[x] -= 1
    dnf = [k for k, v in d.items() if v > 0]
    return dnf[0]

from collections import Counter

def solution(participant, completion):
    d = Counter(participant)
    for i in completion:
        d[i] -= 1
    result = [k for k, v in d.items() if v > 0]
    return result[0]