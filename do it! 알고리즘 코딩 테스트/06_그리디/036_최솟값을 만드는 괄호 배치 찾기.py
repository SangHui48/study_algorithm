import sys
input = lambda : sys.stdin.readline().rstrip()

data = list(input().split('-'))
answer = 0

def summation(i):
    tmp = 0
    tmp_list = str(i).split('+')
    for num in tmp_list:
        tmp += int(num)
    return tmp

for i in range(len(data)):
    tmp = summation(data[i])
    if i == 0:
        answer += tmp
    else:
        answer += (tmp * -1)

print(answer)