n = int(input())
result = 0
for _ in range(n):
    h, b, k = map(int, input().split())
    if b > h:
        result += k * (b - h)
print(result)
