from collections import Counter

def solution(arr):
    answer = 0
    data = Counter(arr)
    col_list = sorted(data.keys(), reverse=True)
    col = 0
    while True:
        flag = False
        possible = 0
        if col == len(col_list):
            break
        if data[col_list[col]] >= 2:
            possible += col_list[col]
            data[col_list[col]] -= 2
            possible_row = []
            for num in col_list:
                if data[num] >= 1:
                    possible_row.append((num, data[num]))
            if len(col_list) == 0:
                flag = True
            else:
                possible_row.sort(key=lambda x:(x[1], -x[0]))
                if possible_row[0][1] > 1:
                    tmp = possible_row[0][0]
                    for row in possible_row:
                        if tmp > row[0]:
                            tmp = row[0]
                    possible += 1
                    data[tmp] -= 1
                else:
                    possible += 1
                    data[possible_row[0][0]] -= 1

        if not flag:
            answer += possible
        else:
            data[col_list[col]] -= 2
        col += 1
    return answer

print(solution([3,3,6,7,7,9]))
print(solution([8,8,3,3,2,2]))
print(solution([5,5,5,5,5]))