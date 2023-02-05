w = int(input())
l = int(input())
h = int(input())

a = min(w, l)
b = max(w, l)
print("good" if a * 2 >= b and a >= h * 2 else "bad")
