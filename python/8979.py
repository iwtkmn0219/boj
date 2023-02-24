n, k = map(int, input().split())
country = []
for _ in range(n):
    country.append(list(map(int, input().split())))
country.sort(key=lambda x: x[1:4], reverse=True)
for i, e in enumerate(country):
    if i == 0:
        e.append(1)
    elif country[i - 1][1:4] == e[1:4]:
        e.append(country[i - 1][4])
    else:
        e.append(i + 1)

    if e[0] == k:
        print(e[4])
        break
