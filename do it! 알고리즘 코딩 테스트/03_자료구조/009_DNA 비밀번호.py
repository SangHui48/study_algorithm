checkSecret = 0 # 몇개의 문자가 관련된 개수를 충족했는가
myList = [0] * 4 # 현재 상태 리스트
checkList = [0] * 4

def myAdd(c):
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def myremove(c):
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1


s, p = map(int, input().split())
result = 0
dna = list(input())
checkList = list(map(int, input().split())) # 비밀번호 체크리스트

for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

for i in range(p):
    myAdd(dna[i])

if checkList == 4:
    result += 1

for i in range(p, s):
    j = i - p
    myAdd(dna[i])
    myremove(dna[j])
    if checkSecret == 4:
        result += 1

print(result)
#
# checkArr = [0] * 4
# myArr = [0] * 4
# checkSecret = 0
#
# def myadd(c):
#     global checkArr, myArr, checkSecret
#     if c == 'A':
#         myArr[0] += 1
#         if myArr[0] == checkArr[0]:
#             checkSecret += 1
#     elif c == 'C':
#         myArr[1] += 1
#         if myArr[1] == checkArr[1]:
#             checkSecret += 1
#     elif c == 'G':
#         myArr[2] += 1
#         if myArr[2] == checkArr[2]:
#             checkSecret += 1
#     elif c == 'T':
#         myArr[3] += 1
#         if myArr[3] == checkArr[3]:
#             checkSecret += 1
#
# def myremove(c):
#     global checkArr, myArr, checkSecret
#     if c == 'A':
#         if myArr[0] == checkArr[0]:
#             checkSecret -= 1
#         myArr[0] -= 1
#     elif c == 'C':
#         if myArr[1] == checkArr[1]:
#             checkSecret -= 1
#         myArr[1] -= 1
#     elif c == 'G':
#         if myArr[2] == checkArr[2]:
#             checkSecret -= 1
#         myArr[2] -= 1
#     elif c == 'T':
#         if myArr[3] == checkArr[3]:
#             checkSecret -= 1
#         myArr[3] -= 1
#
# s, p = map(int, input().split())
# result = 0
# a = list(input())
# checkArr = list(map(int, input().split()))
# for i in range(4):
#     if checkArr[i] == 0:
#         checkSecret += 1
#
# for i in range(p):
#     myadd(a[i])
#
# if checkSecret == 4:
#     result += 1
#
# for i in range(p, s):
#     j = i - p
#     myadd(a[i])
#     myremove(a[j])
#     if checkSecret == 4:
#         result += 1
#
# print(result)