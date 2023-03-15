# https://school.programmers.co.kr/learn/courses/30/lessons/42883
def solution(number, k):
    collected = [] # 여기에 숫자를 한자리씩 채움
    for i, num in enumerate(number):
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)
    # 만약 98765 인 경우면 위 로직에서는 뒤의 넘버가 현제의 넘버보다 클 경우에만 k를 줄이고 수를 빼주기 때문에 아무것도 남지 않을것 따라서 collected가
    # number 리스트와 똑같이 생겻을 것 그 경우를 예외 처리 해주는 코드
    collected = collected[:-k] if k > 0 else collected
    return ''.join(collected)