# https://school.programmers.co.kr/learn/courses/30/lessons/42840
# https://it-garden.tistory.com/197
def solution(answers):
    answer = []
    person_1 = [1,2,3,4,5]
    person_2 = [2,1,2,3,2,4,2,5]
    person_3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == person_1[i % 5]:
            scores[0] +=1
        if answers[i] == person_2[i % 8]:
            scores[1] += 1
        if answers[i] == person_3[i % 10]:
            scores[2] += 1
    for i, score in enumerate(scores):
        if score == max(scores):
            answer.append(i+1)
    return answer