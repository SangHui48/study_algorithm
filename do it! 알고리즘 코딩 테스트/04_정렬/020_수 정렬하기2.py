import sys
input = sys.stdin.readline
print = sys.stdout.write

def merge_sort(start, end):
    if end - start < 1:
        return
    mid = (start + end) // 2
    merge_sort(start, mid)
    merge_sort(mid + 1, end)
    for i in range(start, end+1):
        tmp[i] = data[i]
    k = start
    index_1 = start
    index_2 = mid + 1
    while index_1 <= mid and index_2 <= end:
        if tmp[index_1] > tmp[index_2]:
            data[k] = tmp[index_2]
            k += 1
            index_2 += 1
        else:
            data[k] = tmp[index_1]
            k += 1
            index_1 += 1

    while index_1 <= mid:
        data[k] = tmp[index_1]
        k += 1
        index_1 += 1

    while index_2 <= end:
        data[k] = tmp[index_2]
        k+=1
        index_2 += 1

n = int(input())
data = [0] * (n + 1)
tmp = [0] * (n + 1) # 정려할 때 잠시 사용할 임시 리스트 선언
for i in range(1, n + 1):
    data[i] = int(input())

merge_sort(1, n)

for i in range(1, n+1):
    print(str(data[i]) + '\n')