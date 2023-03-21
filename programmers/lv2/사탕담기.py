# def solution(m, weights):
#     answer = dfs(m, weights, 0, 0)
#     return answer

# def dfs(m, weights, result, start):
#     if result == m:
#         return 1
#     elif result > m:
#         return 0
    
#     if start >= len(weights):
#         return 0
#     return dfs(m, weights, result+weights[start], start+1) + dfs(m, weights, result, start+1)
def dfs(x, i, weights, m):
    global answer
    total = sum([x * y for x, y in zip(weights, x)])
    if total == m:
        answer += 1
        return
    if i >= len(weights) or total > m:
        return
    for j in range(i, len(weights)):
        x[j] = 1
        dfs(x, j+1, weights, m)
        x[j] = 0
answer = 0

def solution(m, weights):
    global x, answer
    x = [0] * len(weights)
    dfs(x, 0, weights, m)
    return answer

def solution(m, weights):
    answer = 0
    def dfs(x, i):
        nonlocal answer
        total = sum([x*y for x, y in zip(weights, x)])
        if total == m:
            answer += 1
            return
        if i >= len(weights) or total > m:
            return
        for j in range(i, len(weights)):
            x[j] = 1
            dfs(x, j + 1)
            x[j] = 0
    x = [0] * len(weights)
    dfs(x, 0)
    return answer

print(solution(3, [500, 1500, 2500, 1000, 2000]))