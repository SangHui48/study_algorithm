# https://school.programmers.co.kr/learn/courses/30/lessons/12977
# https://infinitt.tistory.com/232
# https://velog.io/@koyo/python-is-prime-number
from itertools import combinations
def check(a):
    for i in range(2, int(a ** 1/2) + 1):
        if a % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    cases = list(combinations(nums,3))
    for case in cases:
        if check(sum(case)):
            answer += 1
    return answer