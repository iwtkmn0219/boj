n = int(input())
room = [list(input()) for _ in range(n)]
result = [0, 0]
for r in range(n):
    cnt = 0
    length = 0
    for c in range(n):
        if c == 0 and room[r][c] == ".":
            length = 1
            continue

        if room[r][c] == ".":
            length += 1
        else:
            if length >= 2:
                cnt += 1
            length = 0
    if length >= 2:
        cnt += 1
    result[0] += cnt
for c in range(n):
    cnt = 0
    length = 0
    for r in range(n):
        if r == 0 and room[r][c] == ".":
            length = 1
            continue

        if room[r][c] == ".":
            length += 1
        else:
            if length >= 2:
                cnt += 1
            length = 0
    if length >= 2:
        cnt += 1
    result[1] += cnt
print(*result)
