# https://school.programmers.co.kr/learn/courses/30/lessons/17686
import re
def solution(files):
    answer = [re.split(r"([0-9]+)",file) for file in files]
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(s) for s in answer]