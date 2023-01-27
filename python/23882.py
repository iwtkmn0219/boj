n, k = map(int, input().split())
ls = list(map(int, input().split()))
change_count = 0
for i in range(n - 1, -1, -1):
    if change_count == k:
        break
    idx = -1
    maximum = 0
    for j in range(i + 1):
        if ls[j] > maximum:
            maximum = ls[j]
            idx = j
    if idx < i:
        change_count += 1
    tmp = ls[idx]
    ls[idx] = ls[i]
    ls[i] = tmp
if change_count < k:
    print(-1)
else:
    print(*ls)
