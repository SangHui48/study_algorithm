# https://school.programmers.co.kr/learn/courses/30/lessons/142085
import heapq
def solution(n, k, enemy):
    heap = []
    if k == len(enemy):
        return len(enemy)
    for i in range(len(enemy)):
        if n >= enemy[i]:
            heapq.heappush(heap, -enemy[i])
            n -= enemy[i]
        else:
            if k > 0:
                if heap:
                    a = -heapq.heappop(heap)
                    k -= 1
                    if a > enemy[i]:
                        n += (a - enemy[i])
                        heapq.heappush(heap, -enemy[i])
                    elif a == enemy[i]:
                        heapq.heappush(heap, -enemy[i])
                    else:
                        heapq.heappush(heap, -a)
                else:
                    k -= 1
            else:
                return i
    return len(enemy)

print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
# print(solution(2, 4, [3, 3, 3, 3]))