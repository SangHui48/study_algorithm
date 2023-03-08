# def solution(arr1, arr2):
#     answer = [[] for _ in range(len(arr1))]
#     # def arr_T(arr):
#     #     tmp = [[0 for _ in range(len(arr))] for _ in range(len(arr[0]))]
#     #     for i in range(len(arr)):
#     #         for j in range(len(arr[0])):
#     #             tmp[i][j] = arr[j][i]
#     #     return tmp
#
#     # arr2 = arr_T(arr2)
#     for i in range(len(arr1)):
#         for j in range(len(arr2[0])):
#             val = 0
#             for k in range(len(arr2)):
#                 val += (arr1[i][k] * arr2[k][j])
#             answer[i].append(val)
#     return answer

def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            val = 0
            for k in range(len(arr2)):
                val += (arr1[i][k] * arr2[k][j])
            answer[i].append(val)
    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))