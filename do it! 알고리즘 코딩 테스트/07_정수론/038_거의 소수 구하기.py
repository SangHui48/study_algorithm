import math

a, b = map(int, input().split())
prime_number = [0] * (int(1e7) + 1)

for i in range(2, len(prime_number)):
    prime_number[i] = i

for i in range(2, int(math.sqrt(len(prime_number)))+1):
    if prime_number[i] == 0:
        continue
    for j in range(i + i, len(prime_number), i):
        prime_number[j] = 0

answer = 0
for i in range(2, len(prime_number)):
    if prime_number[i] != 0:
        tmp = prime_number[i]
        while prime_number[i] <= b / tmp: # 자료구조 표현 제약
            if prime_number[i] >= a /tmp:
                answer += 1
            tmp = tmp * prime_number[i]
print(answer)
