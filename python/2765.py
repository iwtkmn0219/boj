def inch_to_miles(x: float) -> float:
    return x / 12 / 5280


PI = 3.1415927
testcase = 1
while True:
    length, rpm, sec = map(float, input().split())
    if rpm == 0:
        break
    distance = inch_to_miles(PI * length * rpm)
    mph = distance / (sec / 3600)
    print(f"Trip #{testcase}: {round(distance, 2)} {round(mph, 2)}")
    testcase += 1
