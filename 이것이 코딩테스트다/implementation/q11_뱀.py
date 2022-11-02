n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 정보
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회정 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 시계 방향 기준, 처음에 오른쪽 보고있음 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 #뱀 머리 위치
    data[x][y] = 2 # 뱀이 존재하면 2
    direction = 0 #맨처음 동쪽 보고있음
    time = 0
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] #뱀이 차지하고 있는 위치 정보
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:
            # 사과가 없을 때
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과 있을 경우
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 자기 몸에 부딪혔을때
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())
