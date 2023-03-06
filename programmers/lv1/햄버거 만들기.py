# https://school.programmers.co.kr/learn/courses/30/lessons/133502
# https://chan-lab.tistory.com/33
# 틀린풀이
# def solution(ingredient):
#     answer = 0
#     idx = 0
#     now = 1
#     while idx < len(ingredient):
#         if ingredient[idx] == now:
#             compare = [1, 3, 2, 1]
#             check = False
#             for i in range(4):
#                 if ingredient[i] != compare[i]:
#                     break
#                 if i == 3 and ingredient[i] == compare[i]:
#                     answer += 1
#                     check = True
#             if check:
#                 for j in range(idx, idx + 4):
#                     ingredient.pop(j)
#
#     return answer

def solution(ingredient):
    answer = 0
    burger = []
    for item in ingredient:
        burger.append(item)
        if burger[-4:] == [1,2,3,1]:
            answer += 1
            for _ in range(4):
                burger.pop()
    return answer