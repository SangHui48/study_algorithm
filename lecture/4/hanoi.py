# n: 옮기려는 원판수
# from_pos: 어디서 출발하는지
# to_pos: 어디로 갈건지
# aux_pos: 중간에 잠시 들르는 기둥
def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, '->', to_pos)
        return
    hanoi(n - 1, from_pos, aux_pos, to_pos)
    print(from_pos, '->', to_pos)
    hanoi(n - 1, aux_pos, to_pos, from_pos)

hanoi(3, 1, 3, 2)

# 1 -> 3
# 1 -> 2
# 3 -> 2
# 1 -> 3
# 2 -> 1
# 2 -> 3
# 1 -> 3