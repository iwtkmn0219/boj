price = [350.34, 230.90, 190.55, 125.30, 180.90]
n = int(input())
for _ in range(n):
    ls = list(map(int, input().split()))
    result = 0
    for i, quantity in enumerate(ls):
        result += price[i] * quantity
    print(f"${result:.2f}")
