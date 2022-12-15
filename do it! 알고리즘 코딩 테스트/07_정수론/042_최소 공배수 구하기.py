import sys
input = lambda : sys.stdin.readline().rstrip()

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    result = a * b / gcd(a, b)
    print(int(result))