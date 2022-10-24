# import heapq
#
# def solution(food_times, k):
#     # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
#     if sum(food_times) <= k:
#         return -1
#
#     # 시간이 적음 음식부터 빼야 하므로 우선순위큐 적용
#     q = []
#     for i in range(len(food_times)):
#         heapq.heappush(q, (food_times[i], i + 1)) # (음식 먹는데 걸리는 시간, 음식 번호)로 우선순위큐 삽입
#
#     sum_value = 0 # 먹기 위해 사용한 시간
#     previous = 0 # 직전에 다 먹은 음식 시간
#     length = len(food_times) # 남은 음식의 개수
#
#     # sum_value + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k를 비교
#     while sum_value + ((q[0][0] - previous) * length) <= k:
#         now = heapq.heappop(q)[0]
#         sum_value += (now - previous) * length
#         length -= 1
#         previous = now
#
#     # 남은 음식 중 몇번쨰 음식인지 확인하여 출력
#     result = sorted(q, key=lambda x: x[1]) #음식 번호순 재정렬
#     return result[(k - sum_value) % length][1]

import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        #(음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간

    length = len(food_times) # 남은 음식의 개수

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식의 개수와 k비교???
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]