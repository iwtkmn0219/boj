t = int(input())
for tc in range(t):
    n = int(input())
    result = 0
    for _ in range(n):
        line = input().split()
        amount = int(line[1])
        price = float(line[2])
        result += amount * price
    print(f"${result:.2f}")
