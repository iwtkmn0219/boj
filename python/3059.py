t = int(input())
for tc in range(t):
    dic = {}
    result = 0
    for i in range(26):
        dic[chr(i + 65)] = i + 65
        result += i + 65
    line = input()
    for i, e in enumerate(line):
        if dic[e] != 0:
            result -= dic[e]
            dic[e] = 0
    print(result)
