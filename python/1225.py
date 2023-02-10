line = input().split()
a = line[0]
b = line[1]
result = 0
for i, ie in enumerate(a):
    for j, je in enumerate(b):
        result += int(ie) * int(je)
print(result)
