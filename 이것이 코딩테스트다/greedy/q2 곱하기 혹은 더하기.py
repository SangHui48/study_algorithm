data = input()
answer = 0
for number in data:
    val = int(number)
    if answer <= 1 or val <= 1:
        answer += val
    else:
        answer *= val

print(answer)