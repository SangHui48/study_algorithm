def solution(seat):
    answer = 0
    reservation = dict()
    for x, y in seat:
        if x not in reservation:
            reservation[x] = [y]
            answer += 1
            continue
        if y not in reservation[x]:
            reservation[x].append(y)
            answer += 1
    return answer

print(solution([[1, 1], [2, 2], [3, 3]]))
print(solution([[1, 1],[2,1],[1,2],[3,4], [2, 1], [2, 1]]))