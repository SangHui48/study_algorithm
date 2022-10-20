# n = int(input())
# data = list(map(int, input().split()))
#
# data.sort(reverse=True)
# answer = 0
# while True:
#     if len(data) == 0:
#         print(answer)
#         break
#
#     data = data[data[0]:]
#     answer += 1

n = int(input())
data = list(map(int, input().split()))
data.sort()

answer = 0
cnt = 0

for x in data:
    cnt += 1
    if cnt >= x:
        answer += 1
        cnt = 0

print(answer)


