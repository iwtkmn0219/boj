import sys

input = sys.stdin.readline

n = int(input())
result = [0, 0]
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        result[0] += 1
    elif a < b:
        result[1] += 1
print(*result)
