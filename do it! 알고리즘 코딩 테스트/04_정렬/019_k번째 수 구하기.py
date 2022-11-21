import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

def quickSort(start, end, k):
    global data
    if start < end:
        pivot = partition(start, end)
        if pivot == k:
            return
        elif k < pivot:
            quickSort(start, pivot-1, k)
        else:
            quickSort(pivot + 1, end, k)

def partition(start, end):
    global data

    if start + 1 == end:
        if data[start] > data[end]:
            data[start], data[end] = data[end], data[start]
        return end

    m = (start + end) // 2
    data[start], data[m] = data[m], data[start]
    pivot = data[start]
    i = start + 1
    j = end

    while i <= j:
        while pivot < data[j] and j > 0:
            j -= 1
        while pivot > data[i] and i < n-1:
            i += 1
        if i <= j:
            data[i], data[j] = data[j], data[i]
            i = i + 1
            j = j - 1

    data[start] = data[j]
    data[j] = pivot
    return j

quickSort(0, n-1, k-1)
print(data[k-1])