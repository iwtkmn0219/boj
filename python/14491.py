def nineth_number(n: int) -> str:
    if n < 9:
        return str(n)
    else:
        return nineth_number(n // 9) + str(n % 9)


n = int(input())
print(nineth_number(n))
