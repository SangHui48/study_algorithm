n, m, k = map(int, input().split())
datas = list(map(int, input().split()))

datas.sort(reverse=True)

pair = (datas[0] * k) + datas[1]

answer = (pair * (m // (k + 1))) + (datas[0] * (m % (k + 1)))
print(answer)