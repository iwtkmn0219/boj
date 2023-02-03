ls = list(map(int, input().split()))
tb = True
for e in ls:
    if e != 0 and e != 1:
        tb = False
if tb:
    print("S")
else:
    print("F")
