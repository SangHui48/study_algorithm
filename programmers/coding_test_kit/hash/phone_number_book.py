from collections import defaultdict

def solution(phone_book):
    phone_book_info = defaultdict(int)

    for phone in phone_book:
        phone_book_info[phone] += 1

    for phone in phone_book:
        tmp = ''

        for num in phone:
            tmp += num
            if tmp in phone_book_info and tmp != phone:
                return False
    return True


# from collections import defaultdict
#
# def solution(phone_book):
#     phone_map = defaultdict(int)
#
#     for number in phone_book:
#         phone_map[number] +=1
#
#     for number in phone_book:
#         tmp = ''
#         for num in number:
#             tmp += num
#             if tmp in phone_map and tmp != number:
#                 return False
#     return True

# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)
#
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True

print(solution(["123", "456", "789"]))