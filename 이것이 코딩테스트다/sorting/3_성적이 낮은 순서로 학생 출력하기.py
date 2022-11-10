n = int(input())
data = []
for _ in range(n):
    x, y = input().split()
    data.append((x, int(y)))
data.sort(key= lambda x: x[1])

for x, y in data:
    print(x, end=' ')