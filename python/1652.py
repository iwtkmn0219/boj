n = int(input())
room = [list(input()) for _ in range(n)]
result = [0, 0]
for r in range(n):
    cnt = 0
    length = 0
    for c in range(n):
        if c == 0:
            length = 1
            continue
        elif c == n - 1 and length >= 2:
            cnt += 1
            continue

        if room[r][c] == ".":
            length += 1
        elif length >= 2:
            cnt += 1
            length = 0
    result[0] += cnt
for c in range(n):
    cnt = 0
    length = 0
    for r in range(n):
        if c == 0:
            length = 1
            continue
        elif c == n - 1 and length >= 2:
            cnt += 1
            continue

        if room[r][c] == ".":
            length += 1
        elif length >= 2:
            cnt += 1
            length = 0
    result[1] += cnt
print(*result)
