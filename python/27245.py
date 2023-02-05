w = int(input())
l = int(input())
h = int(input())
if (0.5 >= min(w, l) / h or min(w, l) / h >= 2) and 0.5 <= w / l <= 2:
    print("good")
else:
    print("bad")
