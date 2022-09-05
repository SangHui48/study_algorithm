n = ord(input())
start = ord('a')

for _ in range(0, n - start + 1):
    print(chr(start), end=' ')
    start += 1