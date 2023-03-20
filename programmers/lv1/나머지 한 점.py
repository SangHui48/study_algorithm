# https://school.programmers.co.kr/learn/courses/18/lessons/1878?language=python3

# def solution(v):
#     answer = []
#     x_dict, y_dict = {}, {}
#     for x, y in v:
#         if x not in x_dict:
#             x_dict[x] = 1
#         else:
#             x_dict[x] += 1
#         if y not in y_dict:
#             y_dict[y] = 1
#         else:
#             y_dict[y] += 1
    
#     for kx, vx in x_dict.items():
#         if vx == 1:
#             answer.append(kx)
#     for ky, vy in y_dict.items():
#         if vy == 1:
#             answer.append(ky)
#     return answer

from collections import Counter
def solution(v):
    answer = []
    x_vals, y_vals = zip(*v)
    x_vals, y_vals = Counter(x_vals), Counter(y_vals)
    for k in x_vals.keys():
        if x_vals[k] == 1:
            answer.append(k)
    for k in y_vals.keys():
        if y_vals[k] == 1:
            answer.append(k)
    return answer

print(solution([[1, 4], [3, 4], [3, 10]]))