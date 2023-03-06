import sys
sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().rstrip()
a = list(input())
b = list(input())
dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
path = []

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(a)][len(b)])

def getText(r, c):
    if r == 0 or c == 0:
        return
    if a[r-1] == b[c-1]:
        path.append(a[r-1])
        getText(r-1, c-1)
    else:
        if dp[r-1][c] > dp[r][c-1]:
            getText(r-1,c)
        else:
            getText(r, c-1)

getText(len(a), len(b))
print(''.join(path[::-1]))