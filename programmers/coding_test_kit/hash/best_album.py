# import operator
# from collections import defaultdict
#
# def solution(genres, plays):
#     music_map = defaultdict(list)
#     rating_map = defaultdict(int)
#     n = len(genres)
#     answer = []
#
#     for i in range(n):
#         music_map[genres[i]].append((i, plays[i]))
#         rating_map[genres[i]] += plays[i]
#
#     rating_map = sorted(rating_map.items(), key=operator.itemgetter(1), reverse=True)
#
#     for info in rating_map:
#         play_info = sorted(music_map[info[0]], key=lambda x: (-x[1]))[:2]
#         for item in play_info:
#             answer.append(item[0])
#
#     return answer

