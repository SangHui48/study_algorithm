# https://school.programmers.co.kr/learn/courses/30/lessons/12985
# 틀린풀이
# def solution(n,a,b):
#     round = 0
#     while True:
#         if 2 ** round >= n:
#             break
#         if (a-1) // 2 + 1 != (b - 1) // 2 + 1:
#             round += 1
#             a = (a - 1)//2 + 1
#             b = (b - 1)//2 + 1
#         else:
#             round += 1
#     return round

def solution(n,a,b):
    answer = 0
    while True:
        a = (a // 2) + (a % 2)
        b = (b // 2) + (b % 2)
        answer += 1
        if a == b:
            return answer
    return answer