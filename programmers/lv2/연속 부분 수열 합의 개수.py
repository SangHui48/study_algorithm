# https://school.programmers.co.kr/learn/courses/30/lessons/131701
def solution(elements):
    n = len(elements)
    elements = elements + elements
    answer = set(elements)
    answer.add(sum(elements))
    for i in range(2, n):
        for j in range(0, n+1):
            answer.add(sum(elements[j:j+i]))
    return len(answer)

print(solution([7,9,1,1,4]))