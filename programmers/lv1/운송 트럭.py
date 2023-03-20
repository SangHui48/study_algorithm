# https://school.programmers.co.kr/courses/16609/lessons/166834
from collections import defaultdict
def solution(max_weight, specs, names):
    answer = 1
    item = defaultdict(int)
    for k, v in specs:
        item[k] = int(v)
    tmp = 0
    for x in names:
        tmp += item[x]
        if tmp > max_weight:
            answer += 1
            tmp = item[x]
    return answer


print(solution(300, [["toy","70"], ["snack", "200"]], ["toy", "snack", "snack"]))
print(solution(200, [["toy","70"], ["snack", "200"]], ["toy", "snack", "toy"]))