fbi_cnt = []
line_number = 0
while True:
    try:
        line = input()
        line_number += 1
        if "FBI" in line:
            fbi_cnt.append(line_number)
    except EOFError:
        if len(fbi_cnt) == 0:
            print("HE GOT AWAY!")
        else:
            print(*fbi_cnt)
        break
