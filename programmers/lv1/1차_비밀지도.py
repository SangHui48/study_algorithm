# https://school.programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    def decode_query(num):
        temp = bin(num)
        binary = temp[2:]
        if len(binary) < n:
            return '0' * (n - len(binary)) + binary
        return binary

    answer = []
    arr1 = list(map(decode_query, arr1))
    arr2 = list(map(decode_query, arr2))
    for i in range(n):
        decode_arr1, decode_arr2 = list(arr1[i]), list(arr2[i])
        temp = ""
        for j in range(n):
            if decode_arr1[j] == '1' or decode_arr2[j] == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    return answer