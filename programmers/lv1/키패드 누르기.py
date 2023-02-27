# https://school.programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    answer = ''
    left, right = 3, 3
    keypad = {'l': [1, 4, 7], 'm': [2, 5, 8, 0], 'r': [3, 6, 9]}
    l_mid, r_mid = False, False
    for num in numbers:
        if num in keypad['l']:
            answer += 'L'
            left = keypad['l'].index(num)
            l_mid = False
        elif num in keypad['r']:
            answer += 'R'
            right = keypad['r'].index(num)
            r_mid = False
        else:
            target = keypad['m'].index(num)
            if l_mid and r_mid:
                if abs(target-left) > abs(target-right):
                    answer += 'R'
                    right = target
                    r_mid = True
                elif abs(target-left) < abs(target-right):
                    answer += 'L'
                    left = target
                    l_mid = True
                else:
                    if hand == 'right':
                        answer += 'R'
                        right = target
                        r_mid=True
                    else:
                        answer += 'L'
                        left = target
                        l_mid = True
                continue
            if l_mid:
                if abs(target - left) > abs(target - right) + 1:
                    answer += 'R'
                    right = target
                    r_mid = True
                elif abs(target - left) < abs(target - right) + 1:
                    answer += 'L'
                    left = target
                    l_mid = True
                elif abs(target - left) == abs(target - right) + 1:
                    if hand == 'right':
                        answer += 'R'
                        right = target
                        r_mid = True
                    elif hand == 'left':
                        answer += 'L'
                        left = target
                        l_mid = True
                continue
            if r_mid:
                if abs(target - left) + 1 > abs(target - right):
                    answer += 'R'
                    right = target
                    r_mid = True
                elif abs(target - left) + 1 < abs(target - right):
                    answer += 'L'
                    left = target
                    l_mid = True
                elif abs(target - left) + 1 == abs(target - right):
                    if hand == 'right':
                        answer += 'R'
                        right = target
                        r_mid = True
                    elif hand == 'left':
                        answer += 'L'
                        left = target
                        l_mid = True
                continue
            if abs(target - left) > abs(target - right):
                answer += 'R'
                right = target
                r_mid = True
            elif abs(target - left) < abs(target - right):
                answer += 'L'
                left = target
                l_mid = True
            else:
                if hand == 'right':
                    answer += 'R'
                    right = target
                    r_mid = True
                elif hand == 'left':
                    answer += 'L'
                    left = target
                    l_mid = True

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))