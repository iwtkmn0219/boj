t = int(input())
for tc in range(t):
    line = list(map(int, input().split()))
    print(line[2] + line[5] + abs(line[3] - line[0]) + abs(line[4] - line[1]))
