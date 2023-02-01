t = int(input())
for tc in range(t):
    row, col = map(int, input().split())
    print(f"사례 #{tc + 1}:")
    for r in range(2 * row + 1):
        if r == 0:
            print(".." + "+-" * (col - 1) + "+")
        elif r == 1:
            print(".." + "|." * (col - 1) + "|")
        else:
            if r % 2 == 0:
                print("+-" * col + "+")
            else:
                print("|." * col + "|")
