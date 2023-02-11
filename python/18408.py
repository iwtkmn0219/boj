ls = list(map(int, input().split()))
one = ls.count(1)
two = ls.count(2)
print(1 if one > two else 2)
