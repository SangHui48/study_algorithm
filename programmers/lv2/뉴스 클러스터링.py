# https://school.programmers.co.kr/learn/courses/30/lessons/17677\
# 오답
# from collections import Counter
# def solution(str1, str2):
#     answer = 0
#     s1, s2 = [], []
#     for i in range(len(str1) - 1):
#         if str1[i].isalpha() and str1[i+1].isalpha():
#             s1.append(str1[i].upper() + str1[i+1].upper())
#     for j in range(len(str2) - 1):
#         if str2[j].isalpha() and str2[j+1].isalpha():
#             s2.append(str2[j].upper() + str2[j+1].upper())
#     s1, s2 = Counter(s1), Counter(s2)
#     cross, union = s1 & s2, s1 | s2
#     if len(cross) == 0 and len(union) == 0:
#         return 65536
#     return int((len(cross) / len(union)) * 65536)

# https://dongdongfather.tistory.com/70
# https://velog.io/@godiva7319/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level2-1%EC%B0%A8-%EB%89%B4%EC%8A%A4-%ED%81%B4%EB%9F%AC%EC%8A%A4%ED%84%B0%EB%A7%81-Python
from collections import Counter
def solution(str1, str2):
    answer = 0
    s1, s2 = [], []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            s1.append(str1[i].upper() + str1[i+1].upper())
    for j in range(len(str2) - 1):
        if str2[j].isalpha() and str2[j+1].isalpha():
            s2.append(str2[j].upper() + str2[j+1].upper())
    s1, s2 = Counter(s1), Counter(s2)
    cross, union = list((s1 & s2).elements()), list((s1 | s2).elements())
    if len(cross) == 0 and len(union) == 0:
        return 65536
    return int((len(cross) / len(union)) * 65536)