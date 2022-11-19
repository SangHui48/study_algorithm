data = list(map(int, input()))

for i in range(len(data)):
    max = i
    for j in range(i + 1, len(data)):
        if data[j] > data[max]:
            max = j

        if data[i] < data[max]:
            data[max], data[i] = data[i], data[max]

print(''.join(list(map(str, data))))