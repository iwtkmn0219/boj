n, k = map(int, input().split())
ls = sorted(list(map(int, input().split())), reverse=True)
print(ls[k - 1])
