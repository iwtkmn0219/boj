def gcd(x: int, y: int) -> int:
    return gcd(y, x % y) if y else x


def find_index(ls: list, x: int) -> int:
    idx = 0
    for i in range(len(position_list) - 1):
        if ls[i + 1] > x:
            return i
    return len(position_list) - 1


n, s = map(int, input().split())
position_list = sorted(list(map(int, input().split())))
position_list = [position_list[0]] + position_list
idx = find_index(position_list, s)
print(gcd(s - position_list[idx], position_list[idx + 1] - s))
