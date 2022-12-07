import sys
input = lambda : sys.stdin.readline().rstrip()
n = int(input())
data = []
for _ in range(n):
    start, end = map(int, input().split())
    data.append((start, end))

data.sort(key= lambda x: (x[1], x[0]))
cnt = 1
end_time = data[0][1]
for i in range(1, len(data)):
    if data[i][0] >= end_time:
        cnt += 1
        end_time = data[i][1]

print(cnt)