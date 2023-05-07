# https://school.programmers.co.kr/learn/courses/30/lessons/42583
# from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     bridge = deque([0 for _ in range(bridge_length)])
#     idx, t_len = 0, len(truck_weights)
#     while bridge:
#         answer += 1
#         bridge.popleft()
#         if idx < t_len:
#             if sum(bridge) + truck_weights[idx] <= weight:
#                 bridge.append(truck_weights[idx])
#                 idx += 1
#             else:
#                 bridge.append(0)
#     return answer

# from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     bridge = deque([0 for _ in range(bridge_length)])
#     idx, t_len = 0, len(truck_weights)
#     sum_bridge = sum(bridge) # 시간초과 발생 방지
#     while bridge:
#         answer += 1
#         bridge.popleft()
#         if idx < t_len:
#             if sum_bridge + truck_weights[idx] <= weight:
#                 bridge.append(truck_weights[idx])
#                 idx += 1
#                 sum_bridge += truck_weights[idx]
#             else:
#                 bridge.append(0)
#     return answer