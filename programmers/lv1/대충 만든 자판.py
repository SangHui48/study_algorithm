# https://school.programmers.co.kr/learn/courses/30/lessons/160586
# test_case 14번부터 실패
def solution(keymap, targets):
    answer = []
    for target in targets:
        cnt = 0
        for s in target:
            idx = 101
            for key_list in keymap:
                if s in key_list:
                    idx = min(idx, key_list.index(s))
            if idx == 101:
                break
            else:
                cnt += (idx + 1)

        if cnt == 0:
            answer.append(-1)
        else:
            answer.append(cnt)
    return answer


def solution(keymap, targets):
    answer = []
    key_dict = {}
    for keys in keymap:
        for i, key in enumerate(keys):
            if key not in key_dict:
                key_dict[key] = i + 1
            else:
                key_dict[key] = min(key_dict[key], i + 1)

    for target in targets:
        cnt = 0
        for key in target:
            if key not in key_dict:
                cnt = -1
                break
            else:
                cnt += key_dict[key]
        answer.append(cnt)
    return answer