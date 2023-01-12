n = int(input())
ls = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i):
        if ls[j] < ls[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(dp[-1])
