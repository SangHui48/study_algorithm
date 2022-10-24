n = int(input())
data = list(input().split())

x = 1
y = 1
directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

for d in data:
    dx = x + directions[d][0]
    dy = y + directions[d][1]

    if 1 <= dx <= n and 1 <= dy <= n:
        x = dx
        y = dy

print(x, y)