dp = [0, 1]
n = int(input())
for _ in range(n):
    tmp = sum(dp)
    dp[0] = dp[1]
    dp[1] = tmp
print(dp[-1])
