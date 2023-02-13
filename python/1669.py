monkey, dog = map(int, input().split())
day_cnt = 0
prev = 0
remaining = dog - monkey
while monkey < dog:
    if prev * 2 < remaining:
        prev += 1
        monkey += prev
    elif prev * 2 > remaining:
        prev = max(prev - 1, 1)
        monkey += prev
    else:
        monkey += prev
    day_cnt += 1
    remaining = dog - monkey
print(day_cnt)
