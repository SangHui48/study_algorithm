import sys
sys.setrecursionlimit(10000)
read = lambda: sys.stdin.readline().rstrip()
n = int(read())

def isPrime(num):
    for i in range(2, int(num/ 2 + 1)):
        if num % i == 0:
            return False
    return True

def dfs(number):
    if len(str(number)) == n:
        print(number)
    else:
        for i in range(1, 10, 2):
            if isPrime(number * 10 + i):
                dfs(number * 10 + i)

dfs(2)
dfs(3)
dfs(5)
dfs(7)