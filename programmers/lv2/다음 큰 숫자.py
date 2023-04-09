# https://school.programmers.co.kr/learn/courses/30/lessons/12911
def solution(n):
    start = n + 1
    while True:
        if bin(n)[2:].count('1') == bin(start)[2:].count('1'):
            return start
        start += 1