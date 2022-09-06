n = int(input())
informations = []
badook_pan = [[0] * 19 for _ in range(19)] # 바둑판
for _ in range(n):
    x, y = map(int, input().split())
    informations.append((x, y)) # x, y좌표

# 좌표값으로 판 채우기
for info in informations:
    badook_pan[info[0] - 1][info[1] - 1] = 1

# 출력
for i in range(19):
    for j in range(19):
        print(badook_pan[i][j], end=' ')
    print()