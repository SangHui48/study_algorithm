def solution(survey, choices):
    point = [3, 2, 1, 0, 1, 2, 3]
    type_point = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(len(survey)):
        type_1, type_2 = survey[i][0], survey[i][1]
        if choices[i] - 1 == 3:
            continue
        if choices[i] - 1 < 3:
            type_point[type_1] += point[choices[i] - 1]
        else:
            type_point[type_2] += point[choices[i] - 1]

    answer = ''

    if type_point['R'] >= type_point['T']:
        answer += 'R'
    else:
        answer += 'T'

    if type_point['C'] >= type_point['F']:
        answer += 'C'
    else:
        answer += 'F'

    if type_point['J'] >= type_point['M']:
        answer += 'J'
    else:
        answer += 'M'

    if type_point['A'] >= type_point['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer