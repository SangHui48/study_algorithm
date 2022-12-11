import math

Min, Max = map(int, input().split())
check = [False] * (Max - Min + 1)

for i in range(2, int(math.sqrt(Max)) + 1):
    start_val = i * i
    start_index = int(Min/start_val)
    if Min % start_val != 0:
        start_index += 1
    for j in range(start_index, int(Max/start_val) + 1):
        check[int(j * start_val) - Min] = True

answer = 0
for i in range(0, Max - Min + 1):
    if not check[i]:
        answer += 1
print(answer)