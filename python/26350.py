n = int(input())
for tc in range(n):
    ls = list(map(int, input().split()))
    print(f"Denominations:", *ls[1:])
    good = True
    for i in range(1, len(ls)):
        if i == 1:
            continue
        if ls[i] < ls[i - 1] * 2:
            good = False
            break
    if good:
        print("Good coin denominations!")
    else:
        print("Bad coin denominations! ")
    if tc < n - 1:
        print()
