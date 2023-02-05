n, m = map(int, input().split())
if n > 7:
    print(n - 7)
else:
    if (m + 14) % 31 == n:
        print(31 - (7 - n))
    elif (m + 14) % 30 == n:
        print(30 - (7 - n))
    elif (m + 14) % 29 == n:
        print(29 - (7 - n))
    else:
        print(28 - (7 - n))
