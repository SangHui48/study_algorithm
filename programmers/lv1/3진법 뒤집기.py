# https://school.programmers.co.kr/learn/courses/30/lessons/68935
def solution(n):
    ten_to_three = []
    while n > 0:
        quotient, remainder = divmod(n, 3)
        ten_to_three.append(str(remainder))
        n = quotient
    return int(''.join(ten_to_three), 3)

print(int('21' , 3))
print(int('123', 4))