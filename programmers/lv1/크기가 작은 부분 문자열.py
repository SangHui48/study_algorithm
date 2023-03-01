# https://school.programmers.co.kr/learn/courses/30/lessons/147355
def solution(t, p):
    answer = 0
    compare = int(p)
    for i in range(0, len(t)-len(p)+1):
        num = int(t[i:i+len(p)])
        if num <= compare:
            answer += 1
    return answer

print(solution("10203", "15"))