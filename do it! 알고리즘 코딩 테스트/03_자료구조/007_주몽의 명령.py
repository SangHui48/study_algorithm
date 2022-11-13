import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
data = list(map(int, input().split()))

data.sort()
i = 0
j = n-1
cnt = 0
while i < j:
    if data[i] + data[j] < m:
        i += 1
    elif data[i] + data[j] > m:
        j -= 1
    else:
        cnt += 1
        i += 1
        j -= 1

print(cnt)