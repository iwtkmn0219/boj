def chk_sort(ls: list) -> bool:
    for i in range(len(ls)):
        if i + 1 != ls[i]:
            return False
    return True


ls = list(map(int, input().split()))
while not chk_sort(ls):
    for i in range(4):
        if ls[i] > ls[i + 1]:
            tmp = ls[i]
            ls[i] = ls[i + 1]
            ls[i + 1] = tmp
            print(*ls)
