# https://school.programmers.co.kr/learn/courses/13213/lessons/91086

import heapq

def solution(no, works):
    if no > sum(works):
        return 0
    works = [-i for i in works]
    heapq.heapify(works)
    
    for _ in range(no):
        w = heapq.heappop(works) + 1
        heapq.heappush(works, w)
    return sum([i ** 2 for i in works])