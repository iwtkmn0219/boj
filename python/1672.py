DNA_DIC = {
    "AA": "A",
    "AG": "C",
    "AC": "A",
    "AT": "G",
    "GA": "C",
    "GG": "G",
    "GC": "T",
    "GT": "A",
    "CA": "A",
    "CG": "T",
    "CC": "C",
    "CT": "G",
    "TA": "G",
    "TG": "A",
    "TC": "G",
    "TT": "T",
}


n = int(input())
s = list(input())
dp = [s] + [[""] * n for _ in range(n - 1)]

for i in range(1, n):
    for j in range(n - i):
        if j == n - i - 1:
            dp[i][j] = DNA_DIC[dp[i - 1][j] + dp[i - 1][j + 1]]
            continue
        dp[i][j] = dp[i - 1][j]
print(dp[n - 1][0])
