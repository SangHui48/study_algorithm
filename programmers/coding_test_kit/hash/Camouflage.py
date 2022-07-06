# from collections import defaultdict
#
# def solution(clothes):
#     answer = 0
#     cloth_info = defaultdict(list)
#
#     for v, k in clothes:
#         cloth_info[k].append(v)
#
#     print(cloth_info)
#     return answer
#
# print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))

# def solution(clothes):
#     from collections import defaultdict
#
#     def solution(clothes):
#         closet = defaultdict(list)
#         for item in clothes:
#             closet[item[1]].append(item[0])
#
#         answer = 1
#
#         for items in closet.values():
#             answer *= (len(items) + 1)
#
#         answer -= 1
#
#         return answer

# from collections import defaultdict
#
# def solution(clothes):
#     answer = 0
#
#     cloth_dict = defaultdict(list)
#
#     for value, key in clothes:
#         cloth_dict[key].append(value)
#
#     combine_list = []
#     combine = 1
#
#     for kind, cloth in cloth_dict.items():
#         answer += len(cloth)
#         combine_list.append(len(cloth))
#
#     if len(combine_list) > 1:
#         for item in combine_list:
#             combine *= item
#
#         answer += combine
#     return answer

from collections import defaultdict

def solution(clothes):
    answer = 1

    cloth_dict = defaultdict(list)

    for value, key in clothes:
        cloth_dict[key].append(value)

    for val in cloth_dict.values():
        answer *= (len(val) + 1)

    answer -= 1

    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))


# def solution(clothes):
#     from collections import Counter
#     from functools import reduce
#     cnt = Counter([kind for name, kind in clothes])
#     answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
#     return answer

