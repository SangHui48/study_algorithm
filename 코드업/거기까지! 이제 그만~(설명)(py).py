n = int(input())
start = 1
sum = 0
while True:
    sum += start
    start += 1
    if sum >= n:
        print(sum)
        break