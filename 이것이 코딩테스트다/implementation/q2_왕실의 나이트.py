start_point = input()
x = ord(start_point[0]) - 96
y = int(start_point[1])

directions = [(1,2),(-1,2),(1,-2),(-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]
cnt = 0

for dy, dx in directions:
    nx = x + dx
    ny = y + dy
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        cnt += 1

print(cnt)