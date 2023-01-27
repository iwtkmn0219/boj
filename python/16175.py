t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    result = [0] * n
    for _ in range(m):
        votes = list(map(int, input().split()))
        for v in range(n):
            result[v] += votes[v]
    print(result.index(max(result)) + 1)
