# def solution(s):
#     answer = len(s)
#     mid = len(s) // 2
#     for i in range(1, mid+1):
#         tmp = ''
#         token = s[:i]
#         count = 1
#         for j in range(i, len(s), i):
#             if token == s[j : j + i]:
#                 count += 1
#             else:
#                 tmp += str(count) + token if count >= 2 else token
#                 token = s[j:j+i]
#                 count = 1
#         tmp += str(count) + token if count >= 2 else token
#         answer = min(answer, len(tmp))
#     return answer

# def solution(s):
#     answer = len(s)
#     i = 1 # 문자열 자르는 단위
#     for i in range(1, len(s) + 1):
#         tmp = ''
#         token = s[:i]
#         cnt = 1
#         for j in range(0, len(s), i):
#             if token == s[j + i:j + 2*i]:
#                 cnt += 1
#             else:
#                 if cnt != 1:
#                     tmp += (str(cnt) + token)
#                     token = s[j : j+i]
#                     cnt = 1
#                 else:
#                     tmp += token
#                     token = s[j:j+i]
#
#             if j + i == len(s):
#                 if cnt != 1:
#                     tmp += (str(cnt) + token)
#                 else:
#                     tmp += token
#         answer = min(answer, len(tmp))
#
#     return answer

def solution(s):
    answer = len(s)
    mid = len(s) // 2
    for i in range(1, mid + 1):
        compressed = ''
        cnt = 1
        token = s[:i]
        for j in range(i, len(s), i):
            if token ==  s[j:j+i]:
                cnt += 1
            else:
                compressed += str(cnt) + token if cnt >= 2 else token
                token = s[j:j+i]
                cnt = 1

        compressed += str(cnt) + token if cnt >= 2 else token
        answer = min(answer, len(compressed))
    return answer

print(solution("aabbaccc"))


def solution(s):
    answer = len(s)

    for size in range(1, len(s) // 2 + 1):
        count = 1
        compress = 0
        
        prev = s[:size]
        for i in range(size, len(s) + size, size):
            curr = s[i:i + size]
            if prev == curr:
                count += 1
            else:
                compress += size + len(str(count)) if 1 < count else len(prev)
                prev = curr
                count = 1
        answer = min(answer, compress)

    return answer