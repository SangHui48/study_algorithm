# def solution(survey, choices):
#     point = [3, 2, 1, 0, 1, 2, 3]
#     type_point = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
#     for i in range(len(survey)):
#         type_1, type_2 = survey[i][0], survey[i][1]
#         if choices[i] - 1 == 3:
#             continue
#         if choices[i] - 1 < 3:
#             type_point[type_1] += point[choices[i] - 1]
#         else:
#             type_point[type_2] += point[choices[i] - 1]
#
#     answer = ''
#
#     if type_point['R'] >= type_point['T']:
#         answer += 'R'
#     else:
#         answer += 'T'
#
#     if type_point['C'] >= type_point['F']:
#         answer += 'C'
#     else:
#         answer += 'F'
#
#     if type_point['J'] >= type_point['M']:
#         answer += 'J'
#     else:
#         answer += 'M'
#
#     if type_point['A'] >= type_point['N']:
#         answer += 'A'
#     else:
#         answer += 'N'
#     return answer

def solution(survey, choices):

    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
    for A,B in zip(survey,choices):
        # survey의 한 요소가 뒤집혀 있으므로
        if A not in my_dict.keys():
            A = A[::-1] #뒤집어 주기 예를 들어서 RT인 경우 TR로 반전 시킨다.
            my_dict[A] -= B-4 # 이후에 choices의 점수만큼 점수를 합산해 주는건데 반대쪽 성격이므로 빼주기
        else:
            my_dict[A] += B-4 # 뒤집어 지지 않았으므로 choices 점수만큼 합산해 준다.

    result = ""
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))