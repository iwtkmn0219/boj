n = int(input())
milk_street = list(map(int, input().split()))
milk_number = [0, 1, 2]
milk_index = 0
cnt = 0
for i, e in enumerate(milk_street):
    if e == milk_number[milk_index]:
        milk_index = (milk_index + 1) % 3
        cnt += 1
print(cnt)
