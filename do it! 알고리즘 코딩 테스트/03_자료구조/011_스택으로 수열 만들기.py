import sys
data_in = sys.stdin.readline

n = int(data_in().rstrip())
data = [0] * n

for i in range(n):
    data[i] = int(data_in().rstrip())

stack = []
num = 1
result = True
answer = ''

for i in range(n):
    tmp = data[i]
    if tmp >= num:
        while tmp >= num:
            stack.append(num)
            num += 1
            answer += '+\n'
        stack.pop()
        answer += '-\n'
    else:
        n = stack.pop()
        if n > tmp:
            print('NO')
            result = False
            break
        else:
            answer += '-\n'

if result:
    print(answer)