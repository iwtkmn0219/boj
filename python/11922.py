dic = {
    "A": [11, 11],
    "K": [4, 4],
    "Q": [3, 3],
    "J": [20, 2],
    "T": [10, 10],
    "9": [14, 0],
    "8": [0, 0],
    "7": [0, 0],
}
n, b = input().split()
result = 0
for _ in range(int(n) * 4):
    line = list(input())
    symbol = line[0]
    suit = line[1]
    if suit == b:
        result += dic[symbol][0]
    else:
        result += dic[symbol][1]
print(result)
