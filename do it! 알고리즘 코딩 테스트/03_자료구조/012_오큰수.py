import sys
data_in = sys.stdin.readline

n = int(data_in().rstrip())
data = list(map(int, data_in().rstrip().split()))
stack = []
answer = [0] * n

for i in range(n):
    while stack and data[stack[-1]] < data[i]:
        answer[stack.pop()] = data[i]
    stack.append(i)

while stack:
    answer[stack.pop()] = -1

for num in answer:
    print(num, end=' ')