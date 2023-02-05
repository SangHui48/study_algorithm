def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
    answer.sort()
    return answer


print('Hello'.isdigit())
print('123'.isdigit())
print('Hello123'.isdigit())