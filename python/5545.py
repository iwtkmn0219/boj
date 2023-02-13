from math import floor

n = int(input())
dough, topping = map(int, input().split())
dough_calorie = int(input())
ls = [0] + sorted([int(input()) for _ in range(n)], reverse=True)
maximum_value = 0
total = dough_calorie
for i, e in enumerate(ls):
    total += e
    value = total / (dough + topping * i)
    if value > maximum_value:
        maximum_value = value
    else:
        break
print(floor(maximum_value))
