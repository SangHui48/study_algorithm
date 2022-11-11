n = int(input())
data = list(map(int, input().split()))
print(sum(data) / (max(data) * len(data)) * 100)