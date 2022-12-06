import heapq
import sys

input = lambda : sys.stdin.readline().rstrip()
n = int(input())
data = []
for _ in range(n):
    heapq.heappush(data, int(input()))

result = 0
while len(data) != 1:
    one = heapq.heappop(data)
    two = heapq.heappop(data)
    sum_value = one + two
    heapq.heappush(data, sum_value)
    result += sum_value

print(result)