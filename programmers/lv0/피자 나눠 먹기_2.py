# https://school.programmers.co.kr/learn/courses/30/lessons/120815
import math

def solution(n):
    divider = math.gcd(n, 6)
    lcm = (6 * n) // divider
    return lcm // 6