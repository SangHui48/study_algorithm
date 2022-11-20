n = int(input())
info = []
for _ in range(n):
    info.append(tuple(map(int, input().split()))) # (x, y) 형태 튜플로 리스트에 넣기

pan = [[0] * 19 for _ in range(19)] # 리스트 컴프리헨션 공부해라 씹새끼야

# pan[1층 ~ 19층][1번째 ~19번쨰]
for x, y in info:
    pan[x-1][y-1] = 1

for i in range(19):
    for j in range(19):
        print(pan[i][j], end=' ')
    print()