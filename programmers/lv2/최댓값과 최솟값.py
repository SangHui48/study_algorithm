# https://school.programmers.co.kr/learn/courses/30/lessons/12939
def solution(s):
    numbers = list(map(int, s.split(' ')))
    return ' '.join(map(str, [min(numbers), max(numbers)]))