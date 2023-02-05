w = int(input())
l = int(input())
h = int(input())
if min(w, l) > h:
    condition1 = min(w, l) >= 2 * h
else:
    condition1 = h >= 2 * min(w, l)
condition2 = max(w, l) <= 2 * min(w, l)
if condition1 and condition2:
    print("good")
else:
    print("bad")
