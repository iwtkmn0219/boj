n = int(input())
for _ in range(n):
    a1, p1 = map(int, input().split())
    r1, p2 = map(int, input().split())
    if (
        a1 * p2
        > 3.14159265358979323846264338327950288419716939937510582097494459
        * r1
        * r1
        * p1
    ):
        print("Slice of pizza")
    else:
        print("Whole pizza")
