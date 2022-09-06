h, w = map(int, input().split())
# 바둑판 초기화
pan = [[0] * w for _ in range(h)]

# 막대기 정보 입력받기
n = int(input())
sticks = []
for _ in range(n):
    sticks.append(tuple(map(int, input().split())))  # 막대 길이, 방향, x, y, 방향의 경우 가로가 0 세로가 1

# 바둑판에 막대 길이 표시
for l, d, x, y in sticks:
    # d = 0 가로
    if d == 0:
        for i in range(l):
            pan[x - 1][y - 1 + i] = 1
    elif d == 1:
        # d = 1 세로
        for j in range(l):
            pan[x - 1 + j][y - 1] = 1

# 출력
for i in range(h):
    for j in range(w):
        print(pan[i][j], end=' ')
    print()
