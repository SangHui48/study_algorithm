n, k = map(int, input().split())
answer = 0
while True:
    if n == 1:
        print(answer)
        break

    if n % k == 0:
        n = n // k
        answer += 1
    else:
        n -= 1
        answer += 1