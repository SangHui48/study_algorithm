# https://school.programmers.co.kr/learn/courses/30/lessons/17687
def convert(base, num):
    tmp = '0123456789ABCDEF'
    a, b = divmod(num,base)
    if a == 0:
        return tmp[b]
    else:
        return convert(base, a) + tmp[b]

def solution(n, t, m, p):
    answer = ''
    full = ''
    for i in range(m*t):
        full += str(convert(n, i))
    
    while len(answer) < t:
        answer += full[p-1]
        p += m
    return answer