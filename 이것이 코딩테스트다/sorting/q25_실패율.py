def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N+1):
        count = stages.count(i)
        if length == 0:
            fail = 0
        else:
            fail = count / length
        answer.append((i, fail))
        length -= count

    answer.sort(key=lambda x:x[1], reverse=True)
    answer = [x[0] for x in answer]
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))