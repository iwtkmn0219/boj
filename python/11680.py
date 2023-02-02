n, m = map(int, input().split())
ls = [0] * 41
for i in range(1, n + 1):
    for j in range(1, m + 1):
        ls[i + j] += 1
maximum = max(ls)
for number, count in enumerate(ls):
    if count == maximum:
        print(number)
