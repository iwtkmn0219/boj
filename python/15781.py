n, m = map(int, input().split())
result = 0
for _ in range(2):
    result += max(list(map(int, input().split())))
print(result)
