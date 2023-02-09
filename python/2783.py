x, y = map(int, input().split())
result = x / y * 1000
for _ in range(int(input())):
    x, y = map(int, input().split())
    result = min(result, x / y * 1000)
print(round(result, 2))
