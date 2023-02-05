n = int(input())
m = int(input())
if n == 1 and m == 1:
    print(1)
elif n == 1:
    print(m)
elif m == 1:
    print(n)
else:
    print(n * 2 + (m - 2) * 2)
