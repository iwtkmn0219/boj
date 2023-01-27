n, m = map(int, input().split())
conv = list(map(int, input().split()))
cnt = [0] * (n + 1)
for c in conv:
    cnt[c] += 1
print(max(cnt))
