def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col-1], -x[0]))
    mod_sum = []
    for i in range(row_begin-1, row_end):
        tmp = 0
        for j in range(len(data[i])):
            tmp += (data[i][j] % (i + 1))
        mod_sum.append(tmp)
    answer = mod_sum[0]
    for i in range(1, len(mod_sum)):
        answer ^= mod_sum[i]
    return answer

print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3))