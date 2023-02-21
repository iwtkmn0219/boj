def gm_number(prev: int):
    if prev > 100000:
        return
    ls.append(prev * 10 + 4)
    ls.append(prev * 10 + 7)
    gm_number(prev * 10 + 4)
    gm_number(prev * 10 + 7)


ls = []
gm_number(0)
ls.sort(reverse=True)
n = int(input())
for e in ls:
    if e <= n:
        print(e)
        break
