# https://school.programmers.co.kr/learn/courses/30/lessons/17682
def solution(dartResult):
    scores = [0, 0, 0]
    multi = {'S': 1, 'D': 2, 'T': 3}
    cnt = -1
    tmp = 0
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if dartResult[i+1].isdigit():
                tmp = 10
                continue
            if tmp != 0:
                cnt += 1
                scores[cnt] = tmp
                tmp = 0
            else:
                cnt += 1
                scores[cnt] = int(dartResult[i])
        else:
            if dartResult[i] in multi:
                scores[cnt] = scores[cnt] ** multi[dartResult[i]]
            else:
                if dartResult[i] == '*':
                    if cnt == 0:
                        scores[0] *= 2
                    else:
                        for j in range(cnt, cnt-2, -1):
                            scores[j] = scores[j] * 2
                elif dartResult[i] == '#':
                    scores[cnt] *= -1
    print(scores)
    return sum(scores)

print(solution('1D*10D#10S*'))