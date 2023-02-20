# https://school.programmers.co.kr/learn/courses/30/lessons/152996
# https://velog.io/@pindum/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%8B%9C%EC%86%8C-%EC%A7%9D%EA%BF%8D-Python
from collections import Counter
def solution(weights):
    answer = 0
    counter = Counter(weights)
    for weight in counter.keys():
        if counter[weight] > 1:
            answer += (counter[weight] * (counter[weight] - 1)) // 2
        if weight * 2 / 3 in counter.keys():
            answer += (counter[weight] * counter[weight * 2/ 3])
        if weight * 2 in counter.keys():
            answer += (counter[weight] * counter[weight * 2])
        if weight * 4 / 3 in counter.keys():
            answer += (counter[weight] * counter[weight * 4 /3])
    return answer

print(solution([100,180,360,100,270]))