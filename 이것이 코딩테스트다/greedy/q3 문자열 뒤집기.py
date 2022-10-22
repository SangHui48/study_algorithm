s = input()

cnt_zero = 0
cnt_one = 0

for i in s:
    if i == '0':
        cnt_zero += 1
    elif i == '1':
        cnt_one += 1



print(min(cnt_one, cnt_zero))