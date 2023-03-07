# https://school.programmers.co.kr/learn/courses/30/lessons/140108
# https://school.programmers.co.kr/questions/41473
import sys
sys.setrecursionlimit(10000)

def solution(s):
    global answer
    answer = 1
    def recursion(s):
        global answer
        start = s[0]
        x, y = 1, 0
        for i, val in enumerate(s[1:]):
            if x == y:
                answer += 1
                return recursion(s[i+1:])
            if i == len(s)-1:
                answer += 1
                break
            if val == start:
                x += 1
            else:
                y += 1
    recursion(s)
    return answer