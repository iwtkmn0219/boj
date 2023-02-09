def axis(x: int) -> tuple:
    return ((x - 1) % 4, (x - 1) // 4)


a, b = map(int, input().split())
print(abs(axis(a)[0] - axis(b)[0]) + abs(axis(a)[1] - axis(b)[1]))
