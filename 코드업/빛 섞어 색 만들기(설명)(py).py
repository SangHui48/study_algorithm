a, b, c = map(int, input().split())
n = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i, j, k)
            n += 1
print(n)