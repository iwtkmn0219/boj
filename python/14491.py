def nineth_number(n: int) -> str:
    if n < 9:
        return str(n)
    else:
        return str(n % 9) + nineth_number(n // 9)


n = int(input())
print(nineth_number(n))
