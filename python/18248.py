n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
possible = True
for i in range(n):
    for j in range(m):
        if not possible:
            break

        if i == 0:
            if a[i][j] == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = 2
            continue

        if j < m - 1:
            if dp[i - 1][j] > dp[i - 1][j + 1]:
                if a[i][j] == 1 and a[i][j + 1] == 0:
                    possible = False
            if dp[i - 1][j] < dp[i - 1][j + 1]:
                if a[i][j] == 0 and a[i][j + 1] == 1:
                    possible = False

        if a[i][j] == 0:
            dp[i][j] = dp[i - 1][j] + 2
        else:
            dp[i][j] = dp[i - 1][j] + 1
print("YES" if possible else "NO")
