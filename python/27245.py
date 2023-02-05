w = int(input())
l = int(input())
h = int(input())
if min(w, l) > h:
    condition1 = min(w, l) / h >= 2
else:
    condition1 = h / min(w, l) >= 2
condition2 = max(w, l) / min(w, l)
if condition1 and condition2:
    print("good")
else:
    print("bad")
