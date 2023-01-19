# import sys
# input = lambda : sys.stdin.readline().rstrip()
#
# class Node(object):
#     def __init__(self, isEnd):
#         self.isEnd = isEnd
#         self.childNode = {}
#
# class Trie(object):
#     def __init__(self):
#         self.parent = Node(None)
#
#     def insert(self, string):
#         nowNode = self.parent
#         temp_length = 0
#         for char in string:
#             # 자식 Node들 미생성된 문자열이면 새로 생성
#             if char not in nowNode.childNode:
#                 nowNode.childNode[char] = Node(char)
#             nowNode = nowNode.childNode[char]
#             temp_length += 1
#             if temp_length == len(string):
#                 nowNode.isEnd = True
#
#
#     def search(self, string):
#         nowNode = self.parent
#         temp_length = 0
#         for char in string:
#             if char in nowNode.childNode:
#                 nowNode = nowNode.childNode[char]
#                 temp_length += 1
#
#                 if temp_length == len(string) and nowNode.isEnd == True:
#                     return True
#             else:
#                 return False
#         return False
#
# n, m = map(int, input().split())
# myTrie = Trie()
#
# for _ in range(n):
#     word = input()
#     myTrie.insert(word)
#
# result = 0
#
# for _ in range(m):
#     word = input()
#     if myTrie.search(word):
#         result += 1
#
# print(result)

import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
textList = set([input() for _ in range(n)])
cnt = 0

for _ in range(m):
    subText = input()
    if subText in textList:
        cnt += 1
print(cnt)