while True:
    line = input().split()
    if line[0] == "#":
        break
    name = line[0]
    age = int(line[1])
    weight = int(line[2])

    print(name, end=" ")
    if age > 17 or weight >= 80:
        print("Senior")
    else:
        print("Junior")
