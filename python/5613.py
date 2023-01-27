result = 100000001
idx = 0
calculate = int()
while True:
    line = input()
    if idx % 2 == 1:
        if line == "+":
            calculate = 0
        elif line == "-":
            calculate = 1
        elif line == "*":
            calculate = 2
        elif line == "/":
            calculate = 3
        else:
            print(result)
            break
        idx += 1
        continue

    line = int(line)
    if idx == 0:
        result = line
    else:
        if calculate == 0:
            result += line
        elif calculate == 1:
            result -= line
        elif calculate == 2:
            result *= line
        elif calculate == 3:
            result //= line
    idx += 1
