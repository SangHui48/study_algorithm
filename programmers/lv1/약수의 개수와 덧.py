# https://school.programmers.co.kr/learn/courses/30/lessons/77884
def div_num(num):
    cnt = 0
    for i in range(1, int(num ** (1/2)) + 1):
        if num % i == 0:
            cnt += 1
            if i ** 2 != num:
                cnt += 1
    return cnt

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        val = div_num(i)
        if val % 2 != 0:
            answer -= i
        else:
            answer += i
    return answer