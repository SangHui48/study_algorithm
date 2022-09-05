n = int(input())
start = 1
sum = 0
while True:
    sum += start
    if sum >= n:
        print(start)
        break
    start += 1