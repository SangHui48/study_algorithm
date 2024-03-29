# https://school.programmers.co.kr/learn/courses/30/lessons/134239
def solution(k, ranges):
    answer = []
    sum_data = [0.0]
    while True:
        next = k * 3 + 1 if k % 2 != 0 else k // 2 # 다음 우박수
        sum_data.append(sum_data[-1] + (k + next) / 2) # 지금 구간에서의 합
        if next == 1: # k가 1이면 종료
            break
        k = next

    for a, offset in ranges:
        b = (len(sum_data) - 1) - (offset*-1)
        if a == b:
            answer.append(0.0)
        elif a < b:
            answer.append(sum_data[b] - sum_data[a]) #구간합 구하기
        else:
            answer.append(-1.0)
    return answer

print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]]))