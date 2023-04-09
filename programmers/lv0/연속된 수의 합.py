#  https://school.programmers.co.kr/learn/courses/30/lessons/120923
# 오답
# def solution(num, total):
#     start = total
#     while True:
#         tmp = sum([x for x in range(start, start-num, -1)])
#         if tmp == total:
#             return sorted([x for x in range(start, start-num, -1)])
#         else:
#             start -= 1

def solution(num, total):
    a1 = (total - ((num*(num-1)//2))) // num
    return [i for i in range(a1, a1+num)]