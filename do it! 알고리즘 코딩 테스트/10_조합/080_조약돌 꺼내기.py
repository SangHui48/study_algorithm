# https://www.acmicpc.net/problem/13251
# m = int(input())
# data = list(map(int, input().split()))
# k = int(input())
# answer = 0
# for num in data:
#     if num >= k:
#         prob = 1
#         tmp = num
#         total_case = sum(data)
#         cnt = 0
#         while  cnt < k:
#             prob *= tmp / total_case
#             tmp -= 1
#             total_case -= 1
#             cnt += 1
#         answer += prob
# print(answer)

m = int(input())
probability = [0] * m
d = list(map(int, input().split()))
k = int(input())

total = sum(d)
answer = 0

for i in range(m):
    if d[i] >= k:
        probability[i] = 1
        for j in range(k):
            probability[i] = probability[i] * (d[i] - j) / (total - j)
        answer += probability[i]
print(answer)