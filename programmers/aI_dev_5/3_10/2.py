import copy
def solution(L, x):
    answer = copy.deepcopy(L)
    idx = 0
    for i in range(len(L)):
        if x < L[i]:
            idx = i
            break
    print(idx)
    if idx != 0:
        answer.insert(idx, x)
    else:
        answer.append(x)
    return answer

print(solution([20, 37, 58], 60))