# s = input()
#
# cnt_zero = 0
# cnt_one = 0
#
# for i in s:
#     if i == '0':
#         cnt_zero += 1
#     elif i == '1':
#         cnt_one += 1
#
#
#
# print(min(cnt_one, cnt_zero))

# s = input()
# cnt0 = 0
# cnt1 = 0
#
# if s[0] == '1':
#     cnt0 += 1
# else:
#     cnt1 += 1
#
# for i in range(1, len(s)-1):
#     if s[i] != s[i+1]:
#         if s[i + 1] == '1':
#             cnt0 += 1
#         else:
#             cnt1 += 1
#
# print(min(cnt0, cnt1))

s = input()
cnt = 0

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt +=1

print((cnt + 1) // 2)