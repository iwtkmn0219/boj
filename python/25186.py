n = int(input())
clothes = list(map(int, input().split()))
closet = {}

if n == 1:
    print("Unhappy")
else:
    happy = True
    for c in clothes:
        if c not in closet:
            closet[c] = 1
        else:
            closet[c] += 1
            if closet[c] > n // 2:
                happy = False
                break
    print("Happy" if happy else "Unhappy")
