n = int(input())
sit = input()
cup_holder = [0] * (n + 1)
idx = 0
while idx < n:
    cup_holder[idx] = 1
    if sit[idx] == "S":
        cup_holder[idx + 1] = 1
    else:
        cup_holder[idx + 2] = 1
        idx += 1
    idx += 1
print(min(n, sum(cup_holder)))
