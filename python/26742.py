line = input()
black = 0
white = 0
for e in line:
    if e == "B":
        black += 1
    else:
        white += 1
print(black // 2 + white // 2)
