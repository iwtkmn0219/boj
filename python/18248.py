n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ls = [[0] * m for _ in range(n)]
possible = True
for i in range(n):
    for j in range(m):
        if not possible:
            break

        if i == 0:
            if a[i][j] == 1:
                ls[i][j] = 1
            else:
                ls[i][j] = 2
            continue

        if j < m - 1:
            if ls[i - 1][j] > ls[i - 1][j + 1]:
                if a[i][j] == 1 and a[i][j + 1] == 0:
                    possible = False
            if ls[i - 1][j] < ls[i - 1][j + 1]:
                if a[i][j] == 0 and a[i][j + 1] == 1:
                    possible = False

        if a[i][j] == 0:
            ls[i][j] = ls[i - 1][j] + 2
        else:
            ls[i][j] = ls[i - 1][j] + 1
print("YES" if possible else "NO")
