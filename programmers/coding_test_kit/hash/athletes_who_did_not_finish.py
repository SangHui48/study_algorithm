from collections import defaultdict

def solution(participant, completion):
    answer = ''

    part_info = defaultdict(int)
    comp_info = defaultdict(int)

    for part_people in participant:
        part_info[part_people] += 1

    for comp_people in completion:
        comp_info[comp_people] += 1

    for key, value in part_info.items():
        if key not in comp_info or value != comp_info[key]:
            answer = key
    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))


# import collections
#
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]