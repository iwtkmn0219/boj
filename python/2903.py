n = int(input())
result = 4
tmp = 2
for i in range(n):
    tmp += 2**i
    result = tmp * tmp
print(result)
