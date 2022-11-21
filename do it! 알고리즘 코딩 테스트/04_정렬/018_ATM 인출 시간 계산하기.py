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

for i in range(1, n):
    insert_point = i
    insert_value = data[i]
    for j in range(i-1, -1, -1):
        if data[j] < data[i]:
            insert_point = j + 1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point, -1):
        data[i] = data[j-1]
    data[insert_point] = insert_value

s[0] = data[0]

for i in range(1, n):
    s[i] = data[i] + s[i-1]

print(sum(s))