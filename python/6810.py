line = "9780921418"
for _ in range(3):
    line += input()
result = 0
for i, e in enumerate(line):
    if i % 2 == 0:
        result += int(e) * 1
    else:
        result += int(e) * 3
print(f"The 1-3-sum is {result}")
