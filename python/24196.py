line = input()
idx = 0
while idx < len(line):
    print(line[idx], end="")
    idx += ord(line[idx]) - ord("A") + 1
