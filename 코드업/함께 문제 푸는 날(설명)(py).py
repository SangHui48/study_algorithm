a, b, c = map(int, input().split())
answer = 2
while True:
    if answer % a == 0 and answer % b == 0 and answer % c == 0:
        print(answer)
        break
    answer += 1