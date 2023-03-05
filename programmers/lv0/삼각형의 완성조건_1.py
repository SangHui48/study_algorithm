# https://school.programmers.co.kr/learn/courses/30/lessons/120889
def solution(sides):
    longest = sides.pop(sides.index(max(sides)))
    if longest < sum(sides):
        return 1
    else:
        return 2