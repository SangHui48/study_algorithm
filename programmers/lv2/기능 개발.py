# https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 처음 풀이 오답
def solution(progresses, speeds):
    result = {}
    for x in range(len(speeds)):
        days = (100 - progresses[x]) // speeds[x]  if (100 - progresses[x]) % speeds[x] == 0 else (100 - progresses[x]) // speeds[x] + 1
        result[days] = result.get(days, 0) + 1
    print(result)
    return [result[x] for x in sorted(result.keys())]

