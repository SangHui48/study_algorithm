# 데이터를 하나씩 확인하며 각 데이터를 적절한 위치에 삽입한다.
# 첫번째 데이터는 정렬되어 있다고 가정 두번째 데이터부터 확인
# 리스트가 정렬되어 있는 상태라면 매우 빠르다.
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)