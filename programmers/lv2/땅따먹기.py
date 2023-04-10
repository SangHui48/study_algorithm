# https://school.programmers.co.kr/learn/courses/30/lessons/12913
# 오답
# def solution(land):
#     answer = 0
#     check = []
#     prev = 4
#     for i in range(len(land)):
#         row = sorted(land[i], reverse=True)
#         max_idx = row.index(row[0])
#         if max_idx == prev:
#             answer += row[1]
#             prev = row.index(row[1])
#         else:
#             answer += row[0]
#             prev = max_idx
#     return answer

# 2번쨰 행부터 시작해서 이전 열을 제외하고 최댓값을 계속 모든 이전행에 누계해준다음 마지막 행을 보고 최댓값을 출력 wow

def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j]+land[i-1][j+1:])
    return max(land[len(land)-1])