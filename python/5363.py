n = int(input())
for line in range(n):
    s = list(input().split())
    print(*s[2:], *s[:2])
