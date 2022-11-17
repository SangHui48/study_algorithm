import sys
data_in = sys.stdin.readline

n = int(data_in().rstrip())
data = list(map(int, data_in().rstrip().split()))
data.reverse()
dp = [1] * n

for i in range(1, n):
     for j in range(0, i):
         if data[j] < data[i]:
             dp[i] = max(dp[i], dp[j] + 1)


print(n - max(dp))