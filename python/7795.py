def binary_search(ls: list, x: int) -> int:
    start = 0
    end = len(ls) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if ls[mid] < x:
            start = mid
        elif ls[mid] >= x:
            end = mid

    if x <= ls[start]:
        return 0
    elif ls[start] < x <= ls[end]:
        return end
    else:
        return len(ls)


t = int(input())
for tc in range(t):
    a_length, b_length = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    # print("A >", A)
    # print("B >", B)
    cnt = 0
    for a in A:
        tmp = binary_search(B, a)
        # print("a >", a, end=', ')
        # print("tmp >", tmp)
        cnt += tmp
    # print("answer >", end=' ')
    print(cnt)
