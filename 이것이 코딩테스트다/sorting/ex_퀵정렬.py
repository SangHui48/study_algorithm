# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다.
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 왼쪽은 피벗보다 큰 데이터
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 오른쪽은 피벗보다 작은 데이터
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 엇갈렷다면 작은 데이터를 피벗과 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 그렇지 않다면 큰수 작은수를 교체
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

