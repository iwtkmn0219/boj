line1 = input()
line2 = input()
result1 = [0] * 26
result2 = [0] * 26
for e in line1:
    result1[ord(e) - ord("A")] += 1
for e in line2:
    result2[ord(e) - ord("A")] += 1
result1.sort()
result2.sort()
result = True
for i in range(26):
    if result1[i] != result2[i]:
        result = False
        break
if result:
    print("YES")
else:
    print("NO")
