ls = [int(input()) for _ in range(4)]
fe = [8, 9]
if ls[0] in fe and ls[3] in fe and ls[1] == ls[2]:
    print("ignore")
else:
    print("answer")
