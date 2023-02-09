n = int(input())
result = 5
for i in range(n - 1):
    result += ((4) + (i + 1) * 3) % 45678
print(result % 45678)
