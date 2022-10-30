n = input()
left = 0
right = 0
for i in range(1, len(n) + 1):
    if i <= len(n) // 2:
        left += int(n[i-1])
    else:
        right += int(n[i-1])

if left == right:
    print('LUCKY')
else:
    print('READY')