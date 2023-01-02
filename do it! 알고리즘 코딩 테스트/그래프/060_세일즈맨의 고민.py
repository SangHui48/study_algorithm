import sys
input = lambda : sys.stdin.readline().rstrip()

n, s_city, e_city, m = map(int, input().split())
edges = []
distance = [-sys.maxsize] * n

for _ in range(m):
    s, e, w = map(int, input().split())
    edges.append((s, e, w))

city_money = list(map(int, input().split()))

# 벤만-포드 시작
distance[s_city] = city_money[s_city]

for i in range(n + 101):
    for start, end, price in edges:
        if distance[start] == -sys.maxsize:
            continue
        elif distance[start] == sys.maxsize:
            distance[end] = sys.maxsize
        elif distance[end] < distance[start] + city_money[end] - price:
            distance[end] = distance[start] + city_money[end] - price
            if i >= n-1:
                distance[end] = sys.maxsize

if distance[e_city] == -sys.maxsize:
    print('gg')
elif distance[e_city] == sys.maxsize:
    print('Gee')
else:
    print(distance[e_city])