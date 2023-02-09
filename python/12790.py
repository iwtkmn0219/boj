n = int(input())
for _ in range(n):
    hp, mp, atk, dif, alpha_hp, alpha_mp, alpha_atk, alpha_dif = map(
        int, input().split()
    )
    total_hp = max(hp + alpha_hp, 1)
    total_mp = max(mp + alpha_mp, 1)
    total_atk = max(atk + alpha_atk, 1)
    total_dif = max(dif + alpha_dif, 1)

    print(total_hp + 5 * total_mp + 2 * total_atk + 2 * total_dif)
