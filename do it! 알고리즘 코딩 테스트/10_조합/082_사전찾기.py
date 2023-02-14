# https://www.acmicpc.net/problem/1256
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=junhyuk7272&logNo=222053814549
# https://bhsmath.tistory.com/153
n, m, k = map(int, input().split())
dp = [[0 for _ in range(n + m + 1)] for _ in range(n + m + 1)]

for i in range(0, n + m + 1):
    for j in range(0, i + 1):
        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
            if dp[i][j] > 1000000000:
                dp[i][j] = 1000000001

if dp[n+m][m] < k:
    print(-1)
else:
    while not (n == 0 and m == 0):
        if dp[n + m - 1][m] >= k:
            print('a', end='')
            n -= 1
        else:
            print('z', end='')
            k -= dp[n + m - 1][m]
            m -= 1