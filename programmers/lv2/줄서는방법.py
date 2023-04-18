# https://school.programmers.co.kr/learn/courses/30/lessons/12936
# https://hongcoding.tistory.com/55
import math
def solution(n, k):
    answer = []
    stack = [i for i in range(1, n+1)]
    k = k - 1
    while stack:
        a = k // math.factorial(n-1)
        answer.append(stack[a])
        del stack[a]
        k = k % math.factorial(n-1)
        n -= 1
    return answer