# 자료구조별 시간 복잡도를 알고 있으면 좋음
# 예를들어서 리스트 -> 탐색 O(N), 딕셔너리, 집합 -> O(1)
# 자료구조별 CRUD 시간복잡도를 알면 굳이 복잡한 알고리즘을 안써도 해결할 수 경우가 많아.

# 지금 같은 리스트
import sys
input = lambda : sys.stdin.readline().rstrip() # 표준입출력

n, m = map(int, input().split())
data = list(map(int, input().split())) # 데이터를 받자마자 합배여을 초기화 할꺼다.
sum = [0]
tmp = 0
for num in data: # 합배열 만들기
    tmp += num
    sum.append(tmp)

loc_info = []
for _ in range(m):
    loc_info.append(tuple(map(int, input().split()))) # 튜플 안쓰면 너가 알게모르게 참조값 바뀌어서 문제 조건값이 바뀌는 많음. 보통 문제에서 주는 조건은 절대 안변하는게 보장되는 자료구조로 받는게 좋음.

for x, y in loc_info:
    print(sum[y] - sum[x-1]) # 리스트는 인덱스로 접근할때는 시간복잡도 1 그래서 고려 안해도돼.

# 문제를 풀때 문제 읽으면서 입력값 받는것까지는 코딩을 해도 좋아. 근데 그 이후에는 이제 코딩을 멈추고 손으로 풀어야돼.
# 첫째, 입력값의 범위를 보고 시간복잡도 유추를 해봐