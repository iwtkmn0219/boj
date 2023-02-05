while True:
    c, d = map(int, input().split())
    if c == 0 and d == 0:
        break
    dic = {"parstel": [30, 40], "parscell": [35, 30], "parsphone": [40, 20]}
    minimum = 9999999999
    for k, v in dic.items():
        minimum = min(minimum, v[0] * c + v[1] * d)
    print(minimum)
