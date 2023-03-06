# https://school.programmers.co.kr/learn/courses/30/lessons/150370
# https://velog.io/@isayaksh/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Programmers-%EA%B0%9C%EC%9D%B8-%EC%A0%95%EB%B3%B4-%EC%88%98%EC%A7%91-%EC%9C%A0%ED%9A%A8%EA%B8%B0%EA%B0%84-Python-7a0bfe4f
# 틀린 풀이 => 문제를 다시 읽어
# from dateutil.relativedelta import relativedelta
# from datetime import datetime
# import dateutil
#
# def solution(today, terms, privacies):
#     answer = []
#     term_kind = {}
#     for term in terms:
#         term, period = term.split()
#         term_kind[term] = int(period)
#     t_year, t_month, t_day = map(int, today.split('.'))
#     now = datetime(t_year, t_month, t_day)
#
#     for info in privacies:
#         start, kind = info.split()
#         year, month, day = map(int, start.split('.'))
#         # print(datetime(today))
#         print(datetime(year, month, day))
#     return answer

# print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))

def convert_date(d):
    year, month, day = map(int, d.split('.'))
    return ((year - 2000) * 12 * 28) + (month * 28) + day


def solution(today, terms, privacies):
    answer = []
    today = convert_date(today)
    term_dict = {}
    for term in terms:
        kind, period = term.split(' ')
        term_dict[kind] = int(period) * 28

    for i, privacy in enumerate(privacies):
        data, kind = privacy.split(' ')
        data = convert_date(data)
        if data + term_dict[kind] <= today:
            answer.append(i + 1)
    return answer