for _ in range(3):
    line = input()
    if len(line) == 1:
        print(1)
        continue
    prev = line[0]
    maximum = 0
    cnt = 1
    for i in range(1, len(line)):
        if line[i] == prev:
            cnt += 1
        else:
            maximum = max(maximum, cnt)
            cnt = 1
            prev = line[i]
    maximum = max(maximum, cnt)
    print(maximum)
