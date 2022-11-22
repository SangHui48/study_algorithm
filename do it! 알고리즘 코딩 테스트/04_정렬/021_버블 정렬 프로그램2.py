import sys
read = lambda: sys.stdin.readline().rstrip()

def merge_sort(start, end):
    global result, data
    if start >= end:
        return
    mid = (start + end) // 2
    merge_sort(start, mid)
    merge_sort(mid+1, end)

    for i in range(start, end+1):
        tmp[i] = data[i]

    k = start
    index_1 = start
    index_2 = mid+1

    while index_1 <= mid and index_2 <= end:
        if tmp[index_1] > tmp[index_2]:
            data[k] = tmp[index_2]
            result += (index_2 - k)
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
        k += 1
        index_2 += 1

# def merge_sort(start, end):
#     global result, data
#     if start < end:
#         mid = (start + end) // 2
#         merge_sort(start, mid)
#         merge_sort(mid+1, end)
#
#         a, b = start, mid+1
#         tmp = []
#
#         while a <= mid and b <= end:
#             if data[a] <= data[b]:
#                 tmp.append(data[a])
#                 a+= 1
#             else:
#                 tmp.append(data[b])
#                 b += 1
#                 result += (mid - a + 1)
#
#         if a <= mid:
#             tmp = tmp + data[a:mid + 1]
#         if b <= end:
#             tmp = tmp + data[b: end+1]
#
#         for i in range(len(tmp)):
#             data[start+i] = tmp[i]

n = int(read())
data = list(map(int, read().split()))
data.insert(0,0)
tmp = [0] * (n + 1)
result = 0

merge_sort(1, n)
print(result)