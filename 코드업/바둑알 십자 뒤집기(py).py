# 바둑판 입력받기
badook_pan = []
for _ in range(19):
    badook_pan.append(list(map(int, input().split())))

#십자 뒤집기 정보 입력받기
n = int(input())
swap_info = []

for _ in range(n):
    swap_info.append(tuple(map(int, input().split())))

# 십자 뒤집기
for x, y in swap_info:
    # 가로 뒤집기
    for i in range(19):
        if badook_pan[x-1][i] == 1:
            badook_pan[x - 1][i] = 0
        else:
            badook_pan[x - 1][i] = 1

    # 세로 뒤집기
    for j in range(19):
        if badook_pan[j][y-1] == 1:
            badook_pan[j][y - 1] = 0
        else:
            badook_pan[j][y - 1] = 1

for i in range(19):
    for j in range(19):
        print(badook_pan[i][j], end=' ')
    print()