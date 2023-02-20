t = int(input())
for tc in range(t):
    n = int(input())
    result = [0, 0]
    for _ in range(n):
        line = input().split()
        if line[0] == line[1]:
            continue
        if line[0] == "R":
            if line[1] == "P":
                result[1] += 1
            elif line[1] == "S":
                result[0] += 1
        elif line[0] == "P":
            if line[1] == "R":
                result[0] += 1
            elif line[1] == "S":
                result[1] += 1
        elif line[0] == "S":
            if line[1] == "R":
                result[1] += 1
            elif line[1] == "P":
                result[0] += 1
    if result[0] == result[1]:
        print("TIE")
    elif result[0] > result[1]:
        print("Player 1")
    else:
        print("Player 2")
