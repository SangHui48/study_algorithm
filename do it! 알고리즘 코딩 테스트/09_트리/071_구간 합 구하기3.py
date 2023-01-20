import sys
input = lambda : sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
treeHeight = 0 # 트리의 높이
length = n # 리프 노드 개수

# 트리 높이 구하기, 리프 노드의 개수를 2씩 나누어 가면서 높이 계산
while length != 0:
    length //= 2
    treeHeight += 1

treeSize = pow(2, treeHeight + 1)
leftNodeStartIndex = treeSize // 2 - 1
tree = [0] * (treeSize + 1)

# 데이터를 리프 노드에 저장
for i in range(leftNodeStartIndex + 1, leftNodeStartIndex + n + 1):
    tree[i] = int(input())

# 인덱스 트리 생성 함수
def setTree(i):
    while i != 1:
        tree[i // 2] += tree[i]
        i -= 1
setTree(treeSize - 1)

# 값 변경 함수
def changeVal(index, value):
    diff = value - tree[index]
    while index > 0:
        tree[index] = tree[index] + diff
        index = index // 2

# 구간 합 구하기
def getSum(s, e):
    partSum = 0
    while s <= e:
        if s % 2 == 1:
            partSum += tree[s]
            s += 1
        if e % 2 == 0:
            partSum += tree[e]
            e -= 1
        s = s // 2
        e = e // 2
    return partSum

for _ in range(m + k):
    query, s, e = map(int, input().split())
    if query == 1:
        changeVal(leftNodeStartIndex + s, e)
    elif query == 2:
        s = s + leftNodeStartIndex
        e = e + leftNodeStartIndex
        print(getSum(s, e))