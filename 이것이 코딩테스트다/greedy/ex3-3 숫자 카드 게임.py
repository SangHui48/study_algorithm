n, m = map(int, input().split())
card_list = []
for _ in range(n):
    card_list.append(list(map(int, input().split())))

answer = 0

for deck in card_list:
    tmp = min(deck)
    # if tmp > answer:
    #     answer = tmp
    answer = max(answer, tmp)

print(answer)