while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    n_line = list(map(int, input().split()))
    m_line = list(map(int, input().split()))
    result = [0] * 10
    for _, n_element in enumerate(n_line):
        for _, m_element in enumerate(m_line):
            tmp = n_element * m_element
            while tmp >= 10:
                result[tmp % 10] += 1
                tmp //= 10
            result[tmp] += 1
    print(*result)
