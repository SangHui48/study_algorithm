s = input()
data = []
total = 0
for i in range(len(s)):
    if s[i].isalpha():
        data.append(s[i])
    else:
        total += int(s[i])
data.sort()
print(''.join(data) + str(total))