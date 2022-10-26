# n, m = map(int, input().split())
# data = list(map(int, input().split()))
#
# result = 0
#
# for i in range(n):
#     for j in range(i+1, n):
#         if data[i] != data[j]:
#             result += 1
#
# print(result)

n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11 # 1부터 10까지의 무게를 담을 수 있는 리스트
for x in data:
    array[x] += 1 # 각 무게에 대해 볼링공의 개수 카운트

result = 0
# 무게 1부터 m까지
for i in range(1, m+1):
    n -= array[i] # 무게가 i인 볼링공의 개수 제외(A가 선택하는 경우)
    result += array[i] * n # B까지 선택했을때 합산

print(result)