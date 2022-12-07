from queue import PriorityQueue
import sys

input = lambda : sys.stdin.readline().rstrip()
plus = PriorityQueue()
minus = PriorityQueue()
one = 0
zeros = 0
n = int(input())
for _ in range(n):
    data = int(input())
    if data > 1:
        plus.put(data * -1)
    elif data == 1:
        one += 1
    elif data == 0:
        zeros += 1
    else:
        minus.put(data)

answer = 0

while plus.qsize() > 1:
    first = plus.get() * -1
    second = plus.get() * -1
    answer += (first * second)

if plus.qsize() > 0:
    answer += (plus.get() * -1)

while minus.qsize() > 1:
    first = minus.get()
    second = minus.get()
    answer += (first * second)

if minus.qsize() > 0:
    if zeros == 0:
        answer += minus.get()

answer += one

print(answer)