n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# data.sort()
# a = data[-1]
# b = data[-2]
# answer = 0
# cnt = 1
# for i in range(m):
#     if cnt % (k + 1) == 0:
#         answer += b
#     else:
#         answer += a
#     cnt += 1
#
# print(answer)

first = data[-1]
second = data[-2]

unit = (first) * k + second
answer = unit * (m // (k + 1)) + (first * (m % (k + 1)))