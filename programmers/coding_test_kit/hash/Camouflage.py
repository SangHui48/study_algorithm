from collections import defaultdict

def solution(clothes):
    answer = 0
    cloth_info = defaultdict(list)

    for v, k in clothes:
        cloth_info[k].append(v)

    print(cloth_info)
    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))

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