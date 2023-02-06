import calendar

def solution(a, b):
    data = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    return data[calendar.weekday(2016, a, b)]

print(solution(5, 24))