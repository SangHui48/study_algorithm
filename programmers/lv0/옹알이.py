# https://school.programmers.co.kr/learn/courses/30/lessons/120956

def solution(babbling):
    answer = 0
    for x in babbling:
        tmp = ""
        cnt = 0
        for s in x:
            tmp += s
            if tmp in ["aya", "ye", "woo", "ma"]:
                tmp = ''
                cnt += 1
        if len(tmp) == 0 and cnt > 0:
            answer += 1
    return answer