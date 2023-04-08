# https://www.acmicpc.net/problem/10807
import sys
input = lambda: sys.stdin.readline().strip()
n = int(input())
data = list(map(int, input().split()))
target = int(input())

print(data.count(target))