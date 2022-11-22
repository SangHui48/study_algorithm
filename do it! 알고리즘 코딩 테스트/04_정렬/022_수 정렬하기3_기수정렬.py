import sys
read = lambda : sys.stdin.readline().rstrip()

n = int(read())
count = [0] * 10001

for i in range(n):
    count[int(read())] += 1

for i in range(len(count)):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)