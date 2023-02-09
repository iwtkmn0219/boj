n = int(input())
ls = list(map(int, input().split()))

maximum_height = 0
prev = 0
height = 0
bottom = 0
for i, e in enumerate(ls):
    if e > prev:
        if i == 0:
            bottom = e
        else:
            height = e - bottom
        if i == len(ls) - 1:
            maximum_height = max(maximum_height, height)
    else:
        maximum_height = max(maximum_height, height)
        height = 0
        bottom = e
    prev = e
print(maximum_height)
