cnt = [0] * 15001
n = int(input())
ls = list(map(int, input().split()))
for e in ls:
    cnt[e] = 1
print(15000 - sum(cnt))
