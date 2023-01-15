n = int(input())
clothes = list(map(int, input().split()))
if n == 1:
    print("Happy")
else:
    print("Happy" if (max(clothes) <= sum(clothes) // 2) else "Unhappy")
