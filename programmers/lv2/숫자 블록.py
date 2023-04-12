# https://school.programmers.co.kr/learn/courses/30/lessons/12923
# 틀린 문제
# import math

# def solution(begin, end):
#     answer = []
#     for i in range(begin, end+1):
#         if i == 1:
#             answer.append(0)
#         else:
#             for j in range(2, int(math.sqrt(i)) + 1):
#                 mok = i // j
#                 if mok > 10 ** 7:
#                     continue
#                 if i % j == 0:
#                     answer.append(mok)
#                     break
#             else:
#                 answer.append(1)
#     return answer

# 역시 처음에 생각했던게 맞았다

def get_divider(n):
    if n == 1:
        return 0
    result = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            result.append(i)
            if n // i <= 10**7:
                return n // i
    if len(result) >= 1:
        return result[-1]
    return 1

def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        res = get_divider(i)
        answer.append(res)
    return answer