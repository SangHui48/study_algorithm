# from collections import defaultdict

# def solution(participant, completion):
#     answer = ''

#     part_info = defaultdict(int)
#     comp_info = defaultdict(int)

#     for part_people in participant:
#         part_info[part_people] += 1

#     for comp_people in completion:
#         comp_info[comp_people] += 1

#     for key, value in part_info.items():
#         if key not in comp_info or value != comp_info[key]:
#             answer = key
#     return answer

from collections import Counter

def solution(participant, completion):
    result = Counter(participant) - Counter(completion)
    return list(result.keys())[0]