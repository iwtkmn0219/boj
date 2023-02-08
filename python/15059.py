als = list(map(int, input().split()))
bls = list(map(int, input().split()))
result = 0
for i in range(3):
    if als[i] < bls[i]:
        result += bls[i] - als[i]
print(result)
