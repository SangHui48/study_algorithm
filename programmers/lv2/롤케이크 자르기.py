# https://school.programmers.co.kr/learn/courses/30/lessons/132265
from collections import Counter
def solution(topping):
    answer = 0
    count_dict = Counter(topping)
    person2 = set()
    while len(topping) > 1:
        now = topping.pop()
        person2.add(now)
        if count_dict[now] > 1:
            count_dict[now] -= 1
        else:
            del count_dict[now]
        if len(person2) == len(count_dict.keys()):
            answer += 1
    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution([1, 2, 3, 1, 4]))