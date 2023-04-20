# https://school.programmers.co.kr/learn/courses/30/lessons/12981
import math
def solution(n, words):
    word_set = set()
    word_set.add(words[0])
    for i in range(1, len(words)):
        player = (i % n) + 1
        if words[i-1][-1] != words[i][0] or words[i] in word_set or len(words[i]) == 1:
            return [player, math.ceil((i+1) / n)]
        else:
            word_set.add(words[i])

    return [0, 0]