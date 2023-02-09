while True:
    ls = sorted(list(map(int, input().split())))
    if ls[0] == 0 and ls[1] == 0 and ls[2] == 0:
        break
    if ls[2] >= ls[0] + ls[1]:
        print("Invalid")
        continue

    if ls[0] == ls[1] == ls[2]:
        print("Equilateral")
    elif ls[0] == ls[1] or ls[1] == ls[2] or ls[0] == ls[2]:
        print("Isosceles")
    else:
        print("Scalene")
