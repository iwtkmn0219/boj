import sys

sys.setrecursionlimit(5000)
input = sys.stdin.readline


def combination(pos: int, cnt: int, value: str) -> None:
    if cnt == 3:
        ls.append(value)
        return
    if pos > 4001:
        return -1

    if cnt == 0:
        combination(pos + 1, cnt + 1, value + str(pos))
    else:
        combination(pos + 1, cnt + 1, value + " " + str(pos))
    combination(pos + 1, cnt, value)


ls = []
combination(1, 0, "")
n, m = map(int, input().split())
graph = [[0] * (4001) for _ in range(4001)]
friend_quantity = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    friend_quantity[a] += 1
    friend_quantity[b] += 1

minimum = 15000
for i, e in enumerate(ls):
    a, b, c = map(int, e.split())
    if graph[a][b] == 1 and graph[b][c] == 1 and graph[c][a] == 1:
        minimum = min(
            minimum, friend_quantity[a] + friend_quantity[b] + friend_quantity[c] - 6
        )
print(minimum if minimum < 15000 else -1)
