n = int(input())
data = list(input().split())

x, y =  1, 1
directinos = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

for i in data:
    dx, dy = directinos[i]
    nx = x + dx
    ny = y + dy
    if 1<= nx <=n and 1 <= ny <=n:
        x = nx
        y = ny

print(x, y)