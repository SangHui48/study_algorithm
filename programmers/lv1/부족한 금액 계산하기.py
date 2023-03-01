# https://school.programmers.co.kr/learn/courses/30/lessons/82612
def solution(price, money, count):
    answer = 0
    accumulation = 0
    for i in range(1, count+1):
        accumulation += (price * i)
    remain = money - accumulation
    if remain < 0:
        return remain * -1
    return answer