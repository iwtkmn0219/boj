n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
friend_quantity = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    friend_quantity[a] += 1
    friend_quantity[b] += 1

minimum = 15000
for i in range(1, n - 1):
    for j in range(i + 1, n):
        if graph[i][j]:
            for k in range(j + 1, n + 1):
                if graph[i][k] == 1 and graph[j][k]:
                    minimum = min(
                        minimum,
                        friend_quantity[i]
                        + friend_quantity[j]
                        + friend_quantity[k]
                        - 6,
                    )
print(minimum if minimum < 15000 else -1)
