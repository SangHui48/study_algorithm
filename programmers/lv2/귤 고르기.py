from collections import Counter
def solution(k, tangerine):
    answer = 0
    data_dict = sorted(Counter(tangerine).items(), key=lambda x: -x[1])
    for item in data_dict:
        answer += 1
        k -= item[1]
        if k <= 0:
            break
    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]	))