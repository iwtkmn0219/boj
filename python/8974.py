ls = [0]
for i in range(50):
    for j in range(i):
        ls.append(i)
a, b = map(int, input().split())
print(sum(ls[a : b + 1]))
