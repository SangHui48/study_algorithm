def solution(L, x):
    idx = 0
    for i in range(len(L)):
        if x > L[i]:
            idx += 1
    L.insert(idx, x)
    return L
print(solution([20, 37, 58, 72, 91], 65))