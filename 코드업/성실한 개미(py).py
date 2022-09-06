# 지도 정보 입력받기
pan = []
for _ in range(10):
    pan.append(list(map(int,input().split())))

# 오른쪽으로 움직이다 벽을 만나면 아래쪽, 근데 다시 오른쪽에 길이 있다면 오른쪽부터
# 먹이를 찾았거나 더이상 움직일 수 없을때까지 오른쪽 -> 아래쪽
# 0 갈수있는곳, 1 벽 또는 장애물, 2 먹이
# 2, 2에서 출발

row = 1
col = 1
while True:
    # index 벗어난경우 종료
    if row == 10 or col == 10:
        break

    # 갈수없을때 아래쪽
    if pan[row][col] == 1:
        col -= 1
        row += 1
    elif pan[row][col] == 2:
        # 먹이발견
        pan[row][col] = 9
        break
    elif pan[row][col] == 0:
        # 갈수 있을때
        pan[row][col] = 9
        col += 1 # 오른쪽 전진

# 결과 출력
for i in range(10):
    for j in range(10):
        print(pan[i][j], end=' ')
    print()