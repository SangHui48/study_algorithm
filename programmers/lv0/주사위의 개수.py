def solution(box, n):
    answer = reduce(lambda x, y: x * y, box)
    return answer