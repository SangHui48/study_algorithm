import sys
input = sys.stdin.readline

n = int(input())
data = [0] * n
for i in range(n):
    data[i] = int(input())

for i in range(n-1):
    for j in range(n-1-i):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]

for num in data:
    print(num)