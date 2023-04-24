# https://school.programmers.co.kr/learn/courses/30/lessons/17684
def solution(msg):
    eng = dict()
    for i in range(26):
        eng[chr(65+i)] = i + 1
    answer = []
    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(eng[msg[w:c]])
            break
        if msg[w:c+1] not in eng:
            eng[msg[w:c+1]] = len(eng) + 1
            answer.append(eng[msg[w:c]])
            w = c
    return answer