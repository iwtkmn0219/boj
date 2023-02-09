level_2017 = [0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6] + [
    0
] * 80
level_2018 = [
    0,
    1,
    2,
    2,
    3,
    3,
    3,
    3,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    4,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
    5,
] + [0] * 80

price_2017 = [0, 500, 300, 200, 50, 30, 10]
price_2018 = [0, 512, 256, 128, 64, 32]

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print((price_2017[level_2017[a]] + price_2018[level_2018[b]]) * 10000)