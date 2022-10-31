# import copy
#
# def rotate(key, m):
#     rst = [[0] * m for _ in range(m)]
#     for i in range(m):
#         for j in range(m):
#             rst[j][m-1-i] = key[i][j]
#
#     return rst
#
# def test(key, lock, i, j, m, n):
#     dump = copy.deepcopy(lock)
#     for p in range(i, i+m):
#         if 0 <= p < n:
#             for q in range(j, j+m):
#                 if 0 <= q < n:
#                     dump[p][q] += key[p-i][q-j]
#
#     for line in dump:
#         for item in line:
#             if item != 1:
#                 return False
#     return True
#
# def solution(key, lock):
#     n, m = len(lock), len(key)
#     for _ in range(4):
#         for i in range(-m+1, n):
#             for j in range(-m+1, n):
#                 if test(key, lock, i, j, m, n):
#                     return True
#         key = rotate(key, m)
#     return False
#
#
# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

def rotate(a):
    m = len(a)
    result = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            result[j][m-1-i] = a[i][j]
    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    m, n = len(key), len(lock)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 3배로 확장한 자물쇠에 정보 갱신
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]

    for rotaion in range(4):
        key = rotate(key)
        for x in range(2 * n):
            for y in range(2 * n):
                # 자물쇠를 열쇠에 대보기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))