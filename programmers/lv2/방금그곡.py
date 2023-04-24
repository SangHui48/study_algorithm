# https://school.programmers.co.kr/learn/courses/30/lessons/17683
# 틀린답
# def convertTime(time):
#     hour, minute = time.split(':')
#     return int(hour) * 60 + int(minute)

# def solution(m, musicinfos):
#     answer = []
#     for musicinfo in musicinfos:
#         s, e, title, codes = musicinfo.split(',')
#         time = convertTime(e) - convertTime(s)
#         # code 맞춰보기
#         for i in range(len(codes)):
#             if i + len(m) > len(codes) - 1:
#                 tmp = codes[i:] + codes[:len(m)-(len(codes))]
#                 if tmp == m:
#                     answer.append((time, title))
#             else:
#                 if codes[i:i+len(m)] == m:
#                     answer.append((time, title))
#     answer.sort(reverse=True, key=lambda x: x[0])
#     if answer:
#         return answer[0][1]
#     else:
#         return None


def convertTime(time):
    hour, minute = time.split(':')
    return int(hour) * 60 + int(minute)

def changeCode(codes):
    codes = codes.replace('C#', 'c')
    codes = codes.replace('D#', 'd')
    codes = codes.replace('F#', 'f')
    codes = codes.replace('G#', 'g')
    codes = codes.replace('A#', 'a')
    return codes

def solution(m, musicinfos):
    answer = []
    m = changeCode(m)
    for idx, musicinfo in enumerate(musicinfos):
        s, e, title, codes = musicinfo.split(',')
        time = convertTime(e) - convertTime(s)
        codes = changeCode(codes)
        play = codes * (time // len(codes)) + codes[:time % len(codes)]
        if m in play:
            answer.append((time, idx, title))
    answer.sort(key=lambda x: (-x[0], x[1]))
    if answer:
        print(answer)
        return answer[0][2]
    else:
        return None
    

print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))


# def convertTime(time):
#     hour, minute = time.split(':')
#     return int(hour) * 60 + int(minute)

# def changeCode(codes):
#     codes = codes.replace('C#', 'c')
#     codes = codes.replace('D#', 'd')
#     codes = codes.replace('F#', 'f')
#     codes = codes.replace('G#', 'g')
#     codes = codes.replace('A#', 'a')
#     return codes

# def solution(m, musicinfos):
#     answer = []
#     for idx, musicinfo in enumerate(musicinfos):
#         target = changeCode(m)
#         s, e, title, codes = musicinfo.split(',')
#         time = convertTime(e) - convertTime(s)q
#         codes = changeCode(codes)
#         play = codes * (time // len(codes)) + codes[:time % len(codes)]
#         if target in play:
#             answer.append((time, idx, title))
#     answer.sort(key=lambda x: (-x[0], x[1]))
#     if answer:
#         return answer[0][2]
#     else:
#         return None

def convertTime(time):
    hour, minute = time.split(':')
    return int(hour) * 60 + int(minute)

def changeCode(codes):
    codes = codes.replace('C#', 'c')
    codes = codes.replace('D#', 'd')
    codes = codes.replace('F#', 'f')
    codes = codes.replace('G#', 'g')
    codes = codes.replace('A#', 'a')
    return codes

def solution(m, musicinfos):
    answer = []
    for idx, musicinfo in enumerate(musicinfos):
        target = changeCode(m)
        s, e, title, codes = musicinfo.split(',')
        time = convertTime(e) - convertTime(s)
        codes = changeCode(codes)
        play = codes * (time // len(codes)) + codes[:time % len(codes)]
        if target in play:
            answer.append((time, idx, title))
    answer.sort(key=lambda x: (-x[0], x[1]))
    if answer:
        return answer[0][2]
    else:
        return "(None)"