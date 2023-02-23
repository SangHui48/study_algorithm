# https://school.programmers.co.kr/learn/courses/30/lessons/131127
from collections import Counter
def solution(want, number, discount):
    answer = 0
    wish_dict = {}
    for i in range(len(want)):
        wish_dict[want[i]] = number[i]
    for i in range(0, len(discount)-9):
        target_dict = Counter(discount[i:i+10])
        if target_dict == wish_dict:
            answer += 1
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))