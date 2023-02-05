ls = list(map(int, input().split()))
if ls[0] * ls[1] > ls[2] * ls[3]:
    print("M")
elif ls[0] * ls[1] > ls[2] * ls[3]:
    print("P")
else:
    print("E")
