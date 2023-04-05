# https://www.acmicpc.net/problem/27932

from sys import stdin as s
import bisect

s = open('/Users/hansanghui/Documents/GitHub/study_algorithm/input.txt', 'rt')
n, k = map(int, s.readline().strip().split())
students = list(map(int, s.readline().strip().split()))

ans = 0
h = 0 # 이웃한 사람과의 차이
while True:
    tired = 0 # 지친 사람의 갯수
    for i in range(len(students)):
        if i == 0:
            if abs(students[i] - students[i+1]) > h:
                tired += 1
        elif i == (len(students) - 1):
            if abs(students[i] - students[i-1]) > h:
                tired += 1
        else:
            if abs(students[i] - students[i+1]) > h or abs(students[i] - students[i-1]) > h:
                tired += 1

    if tired <= k:
        ans = h
        break
    
    h += 1

print(ans)
    