from math import sqrt

n = int(input())
result = 0
for i in range(1, int(sqrt(n)) + 1):
    if n % i == 0:
        result += i
        if i * i != n:
            result += n // i
print(result)
