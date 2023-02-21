cnt = [0] * 26
while True:
    try:
        line = input()
        for e in line:
            if e == " ":
                continue
            cnt[ord(e) - ord("a")] += 1
    except EOFError:
        maximum = max(cnt)
        for i, e in enumerate(cnt):
            if e == maximum:
                print(chr(i + ord("a")), end="")
        break
