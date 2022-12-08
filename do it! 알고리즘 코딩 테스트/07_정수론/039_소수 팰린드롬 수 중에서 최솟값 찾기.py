import math

n = int(input())
prime_number = [0] * (int(1e7) + 1)

for i in range(2, int(1e7) + 1):
    prime_number[i] = i

for i in range(2, int(math.sqrt(int(1e7) + 1))):
    if prime_number[i] == 0:
        continue
    for j in range(i + i, int(1e7) + 1, i):
        prime_number[j] = 0

def isPalin(target):
    tmp = list(str(target))
    s = 0
    e = len(tmp) - 1
    while s < e:
        if tmp[s] != tmp[e]:
            return False
        s += 1
        e -= 1
    return True

i = n
while True:
    if prime_number[i] != 0:
        result = prime_number[i]
        if isPalin(result):
            print(result)
            break
    i += 1