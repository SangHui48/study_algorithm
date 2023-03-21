def dfs(level, s):
    if level == r:
        print(result)
        return
    for i in range(s, len(n)):
        result[level] = n[i]
        dfs(level+1, i+1)
        
n = [i for i in range(10)]
r = 6
result = [0] * r
dfs(0, 0)