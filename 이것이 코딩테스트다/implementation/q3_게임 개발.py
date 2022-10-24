# n, m = map(int,input().split())
# a, b, d = map(int,input().split())
#
# info = []
# for _ in range(n):
#     info.append(list(map(int, input().split())))
#
# directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북 동 남 서
# while True:
#     d -= 1
#     if d < 0:
#         d += 4

n, m = map(int, input().split())

# 방문위치 저장
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 x 좌표, y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

cnt = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    else:
        # 회전 이후 가보지 않은 칸이 없거나 바다일때
        turn_time += 1

    # 네 방향 모두 못갓을때
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(cnt)