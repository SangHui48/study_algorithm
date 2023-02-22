from math import gcd
from functools import reduce
def solution(arrayA, arrayB):
    gcd_A = reduce(gcd, arrayA)
    gcd_B = reduce(gcd, arrayB)
    for idx, num_a in enumerate(arrayA):
        if num_a % gcd_B == 0:
            break
        if idx == len(arrayA) - 1:
            return max(gcd_A, gcd_B)
    for idx, num_b in enumerate(arrayB):
        if num_b % gcd_A == 0:
            break
        if idx == len(arrayB) - 1:
            return max(gcd_A, gcd_B)
    return 0

print(solution([10, 17], [5, 20]))
print(solution([10, 20], [5, 17]))
print(solution([14, 35, 119], [18, 30, 102]))