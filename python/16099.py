t = int(input())
for tc in range(t):
    ls = list(map(int, input().split()))
    e = ls[0] * ls[1]
    tpt = ls[2] * ls[3]
    if e == tpt:
        print("Tie")
    elif e > tpt:
        print("TelecomParisTech")
    else:
        print("Eurecom")
