n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]

for col in range(n):
    cnt = 0
    max_height = 0
    for row in range(n):
        if forest[row][col] > max_height:
            cnt += 1
            max_height = forest[row][col]
    print(cnt, end=" ")
print()
for row in range(n):
    cnt = 0
    max_height = 0
    for col in range(n):
        if forest[row][col] > max_height:
            cnt += 1
            max_height = forest[row][col]
    print(cnt)
