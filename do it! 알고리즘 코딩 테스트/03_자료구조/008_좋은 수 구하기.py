import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()
cnt = 0

for k in range(n):
    find = data[k]
    i = 0
    j = n-1
    while i < j:
        if data[i] + data[j] == find:
            if i != k and j != k:
                cnt += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif data[i] + data[j] < find:
            i += 1
        else:
            j -= 1
print(cnt)
