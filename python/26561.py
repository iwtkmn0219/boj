t = int(input())
for tc in range(t):
    p, t = map(int, input().split())
    print(p - t // 7 + t // 4)
