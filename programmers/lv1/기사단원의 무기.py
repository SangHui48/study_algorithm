# https://school.programmers.co.kr/learn/courses/30/lessons/136798
def solution(number, limit, power):
    answer = 0

    def get_div_num(num):
        cnt = 0
        for i in range(1, int(num ** (1 / 2)) + 1):
            if num % i == 0:
                cnt += 1
                if i ** 2 != num:
                    cnt += 1
        return cnt

    knights = []
    for i in range(1, number + 1):
        knights.append(get_div_num(i))
    for knight in knights:
        if knight <= limit:
            answer += knight
        else:
            answer += power
    return answer