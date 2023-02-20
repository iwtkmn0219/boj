n = int(input())
m = int(input())
target_list = list(map(int, input().split()))
result = [0] * n
for target in target_list:
    line = list(map(int, input().split()))
    for i, answer in enumerate(line):
        if target == answer:
            result[i] += 1
        else:
            result[target - 1] += 1
for r in result:
    print(r)
