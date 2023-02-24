n = int(input())
people = [input() for _ in range(n)]
inc_peo = sorted(people)
dec_peo = sorted(people, reverse=True)
if people == inc_peo:
    print("INCREASING")
elif people == dec_peo:
    print("DECREASING")
else:
    print("NEITHER")
