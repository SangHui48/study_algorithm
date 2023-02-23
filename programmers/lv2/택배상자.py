# https://school.programmers.co.kr/learn/courses/30/lessons/131704
from collections import deque
def solution(order):
    answer = 0
    order = deque(order)
    stack = []
    for i in range(1, len(order) + 1):
        stack.append(i)
        while stack and order[0] == stack[-1]:
            answer += 1
            stack.pop()
            order.popleft()
    return answer