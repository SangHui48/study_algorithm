# https://school.programmers.co.kr/learn/courses/30/lessons/12951
def solution(s):
    return ' '.join([word.capitalize() for word in s.split(' ')])