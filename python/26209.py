ls = list(map(int, input().split()))
tb = True
for e in ls:
    if e != 0 and e != 1:
        print("F")
        tb = False
if tb:
    print("S")
