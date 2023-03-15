# https://school.programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    uniform = [1] * (n + 2)
    for i in reserve:
        uniform[i] += 1
    for i in lost:
        uniform[i] -= 1

    for i in range(1, n+1):
        if uniform[i-1] == 0 and uniform[i] == 2:
            uniform[i-1:i+1] = [1, 1]
        elif uniform[i] == 2 and uniform[i+1] == 0:
            uniform[i:i+2] = [1, 1]

    return len([x for x in uniform[1:-1] if x > 0])

def solution(n, lost, reserve):
    s = set(lost) & set(reserve)
    l = set(lost) - s
    r = set(reserve) - s
    for x in sorted(r):
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)
    return n - len(l)