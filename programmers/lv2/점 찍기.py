# https://school.programmers.co.kr/learn/courses/30/lessons/140107
def solution(k, d):
    answer = 0
    for x in range(0, d+1, k):
        y_range = int((d**2 - x**2)**0.5)
        answer += (y_range // k) + 1
    return answer

print(solution(2, 4))
print(solution(1, 5))