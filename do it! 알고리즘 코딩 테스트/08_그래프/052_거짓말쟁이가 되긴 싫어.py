n, m = map(int, input().split())
true_person = list(map(int, input().split()))
T = true_person[0]
del true_person[0]
result = 0
party = []
for _ in range(m):
    party.append(list(map(int, input().split())))


parent = [i for i in range(n + 1)]

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def checkSame(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for i in range(m):
    first_person = party[i][1]
    for j in range(2, len(party[i])):
        union(first_person, party[i][j])

for i in range(m):
    isPossible = True
    first_person = party[i][1]
    for j in range(len(true_person)):
        if find(first_person) == find(true_person[j]):
            isPossible = False
            break

    if isPossible:
        result += 1

print(result)