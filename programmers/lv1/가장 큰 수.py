# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x: (x*4)[:4], reverse=True)
    return str(int(''.join(numbers)))

print(solution([0,0]))