n = int(input())
cnt = 0

wallet = [500, 100, 50, 10]

for coin in wallet:
    cnt += n // coin
    n = n % coin

print(cnt)