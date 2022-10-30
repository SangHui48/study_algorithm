n, k = map(int, input().split())
answer = 0
while n >= k:
    if n//k != 0 :
        n = n % k
        answer += 1
    else :
        n-=1
        answer += 1
answer += n
print(answer)