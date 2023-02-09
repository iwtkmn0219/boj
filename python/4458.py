n = int(input())
for _ in range(n):
    line = input().split()
    for _, e in enumerate(line):
        print(e[0].upper() + e[1:], end=" ")
    print()
