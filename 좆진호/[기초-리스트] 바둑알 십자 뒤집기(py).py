# 판입력
pan_info = []
for _ in range(19):
    pan_info.append(list(map(int, input().split())))
n = int(input())
change = []
for _ in range(n):
    change.append(tuple(map(int, input().split())))

for x, y in change:
    # 가로방향 바꾸고(y)
    for i in range(19):
        if pan_info[x-1][i] == 0:
            pan_info[x-1][i] = 1
        elif pan_info[x-1][i] == 1:
            pan_info[x-1][i] = 0
    # 세로방향 바꾸고(x)
    for j in range(19):
        if pan_info[j][y-1] == 0:
            pan_info[j][y-1] = 1
        elif pan_info[j][y-1] == 1:
            pan_info[j][y-1] = 0

for i in range(19):
    for j in range(19):
        print(pan_info[i][j], end=' ')
    print()