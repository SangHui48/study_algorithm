# https://school.programmers.co.kr/learn/courses/30/lessons/17680
# https://j2wooooo.tistory.com/121
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    queue = deque([])
    cities = [i.lower() for i in cities]
    for city in cities:
        if cacheSize:
            if city in queue:
                answer += 1
                queue.remove(city)
                queue.append(city)
            else:
                if len(queue) == cacheSize:
                    queue.popleft()
                    queue.append(city)
                    answer += 5
                else:
                    queue.append(city)
                    answer += 5
        else:
            answer += 5
    return answer