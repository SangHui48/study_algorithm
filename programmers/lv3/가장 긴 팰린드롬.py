# https://school.programmers.co.kr/learn/courses/30/lessons/12904

def solution(s):
    answer = ''
    for answer in range(len(s), 0, -1):
        start = 0
        end = answer - 1
        while end < len(s):
            if s[start:end+1] == s[start:end+1][::-1]:
                return answer
            start += 1
            end += 1
    return answer
print(solution("abcdcba"))