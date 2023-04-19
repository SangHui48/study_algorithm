# https://school.programmers.co.kr/learn/courses/30/lessons/12953
def solution(arr):
    def gcd(a , b):
        while b:
            a, b = b, a % b
        return a
    answer = arr[0]
    for num in arr:
        answer = (num * answer) // gcd(answer, num)
    return answer