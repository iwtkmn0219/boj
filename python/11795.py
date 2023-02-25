n = int(input())
result = [0, 0, 0]
for _ in range(n):
    tmp = list(map(int, input().split()))
    for i in range(len(result)):
        result[i] += tmp[i]
    mini = min(result)
    if mini >= 30:
        for i in range(len(result)):
            result[i] -= mini
        print(mini)
    else:
        print("NO")
