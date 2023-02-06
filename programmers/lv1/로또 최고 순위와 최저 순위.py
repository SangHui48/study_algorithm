def solution(lottos, win_nums):
    if lottos.count(0) == 6:
        return [1, 6]
    rank = 6
    possible = 0
    cnt = 0
    for num in lottos:
        if num in win_nums:
            cnt += 1
            if cnt >= 2:
                rank -= 1
        if num == 0:
            possible += 1
    return [rank-possible, rank]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))