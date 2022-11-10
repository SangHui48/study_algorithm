# n = int(input())
# data = []
# for _ in range(n):
#     data.append(int(input()))
#
# data.sort()
# index = 0
# answer = 0
# prev = 0 # 누적
# while index < n:
#     if index > 1:
#         answer = answer + answer + data[index]
#         index += 1
#     else:
#         answer += data[index]
#         index += 1
#
# print(answer)

import heapq

n = int(input())
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)