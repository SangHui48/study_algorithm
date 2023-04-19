# https://school.programmers.co.kr/learn/courses/30/lessons/12973
# 틀린풀이
# def solution(s):
#     answer = 0
#     while True:
#         flag = False
#         if len(s) == 2 and (s[0] == s[1]):
#             return 1
#         for i in range(len(s)-1):
#             if s[i] == s[i+1]:
#                 if i == 1:
#                     s = s[0] + s[i+2:]
#                 else:
#                     s = s[:i-1] + s[i+2:]
#                 flag = True
#                 break
#         if not flag:
#             return 0
#     return answer

def solution(s):
    stack = []
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        elif stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    if stack:
        return 0
    else:
        return 1
