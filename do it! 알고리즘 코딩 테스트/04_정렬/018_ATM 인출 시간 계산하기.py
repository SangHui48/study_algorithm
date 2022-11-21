import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
s = [0] * n

# for i in range(n):
#     min_index = i
#     for j in range(i+1, n):
#         if data[j] < data[min_index]:
#             min_index = j
#     data[i] , data[min_index] = data[min_index], data[i]

s[0] = data[0]

for i in range(1, n):
    s[i] = data[i] + s[i-1]

print(sum(s))