import heapq
from collections import deque

def solution(healths, items):
    healths.sort()
    items = sorted([(item[1], item[0], index+1) for index, item in enumerate(items)])
    items = deque(items)
    answer = []
    heap = []
    for health in healths:
        while items:
            debuff, buff, index = items[0]
            if health - debuff < 100:
                breakq
            items.popleft()
            heapq.heappush(heap, (-buff, index))
        if heap:
            _, index = heapq.heappop(heap)
            answer.append(index)
    return sorted(answer)


print(solution([200,120,150], [[30,100],[500,30],[100,400]]))