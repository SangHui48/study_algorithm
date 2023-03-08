# https://school.programmers.co.kr/learn/courses/30/lessons/12922
def solution(n):
    answer = ''
    data = {0: '수', 1:'박'}
    for i in range(n):
        answer += data[i % 2]
    return answer