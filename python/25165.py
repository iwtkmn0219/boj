n, m = map(int, input().split())
a, d = map(int, input().split())
r, c = map(int, input().split())
direction = [1, -1]
d_idx = 0 if d == 1 else 1
x = a - 1
y = 0
monster = False
while x < m and y < n:
    xx = x + direction[d_idx]
    if 0 <= xx < m:
        x = xx
    else:
        d_idx = (d_idx + 1) % 2
        y += 1
    if x == c - 1 and y == r - 1:
        monster = True
        break
if monster:
    print("NO...")
else:
    print("YES!")
