# 가장 작은 데이터를 선택해 맨앞에 두고 그다음 작은 데이터를 선택해 그 다음에 두고... 끝날때까지 반복
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i] , array[min_index] = array[min_index], array[i]

print(array)