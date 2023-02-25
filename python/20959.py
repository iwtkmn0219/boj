line = input()
result = ""
for e in line:
    if e.isdigit():
        result += e
    else:
        result += " "
result = result.split()
dic = {}
for e in result:
    if e not in dic:
        dic[e] = 1
print(len(dic))
