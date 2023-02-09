n = int(input())
ls = []
for _ in range(n):
    ls.append(int(input()))
maximum_height = 0
cnt = 0
for i in range(n - 1, -1, -1):
    if ls[i] > maximum_height:
        maximum_height = ls[i]
        cnt += 1
print(cnt)
