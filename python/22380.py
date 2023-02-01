while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    people_list = list(map(int, input().split()))
    money = 0
    for _, e in enumerate(people_list):
        if e >= m // n:
            money += m // n
        else:
            money += e
    print(money)
