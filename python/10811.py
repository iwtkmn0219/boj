n, m = map(int, input().split())
ls = [i for i in range(n + 1)]
for _ in range(m):
    s, e = map(int, input().split())
    tmp = ls[:s] + ls[e : s - 1 : -1] + ls[e + 1 :]
    ls = tmp
print(*tmp[1:])
