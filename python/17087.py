def gcd(x: int, y: int) -> int:
    return gcd(y, x % y) if y else x


n, s = map(int, input().split())
position_list = list(map(int, input().split()))
result = abs(s - position_list[0])
for i in range(1, len(position_list)):
    tmp = abs(s - position_list[i])
    result = gcd(result, tmp)
print(result)
