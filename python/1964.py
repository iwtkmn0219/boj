n = int(input())
ls = [0, 5]
for i in range(n - 1):
    ls.append(ls[-1] + (4) + (i + 1) * 3)
print(ls[-1])
