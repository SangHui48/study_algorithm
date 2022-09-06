n = int(input())
answers = [0] * 23
order = list(map(int,input().split()))

for i in order:
    answers[i-1] += 1

for answer in answers:
    print(answer, end=' ')