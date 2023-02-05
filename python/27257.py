line = input()
result = 0
zero = 0
for i, e in enumerate(line):
    if e == "0":
        zero += 1
    else:
        result += zero
        zero = 0
print(result)
