t = int(input())
for tc in range(t):
    p, q = map(int, input().split())
    print(f"{round(1 / (1 / p + 1 / q), 2)}")
