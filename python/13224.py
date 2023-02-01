def move_atype(ls: list):
    tmp = ls[0]
    ls[0] = ls[1]
    ls[1] = tmp


def move_btype(ls: list):
    tmp = ls[1]
    ls[1] = ls[2]
    ls[2] = tmp


def move_ctype(ls: list):
    tmp = ls[0]
    ls[0] = ls[2]
    ls[2] = tmp


BALL = "o"
EMPTY = "x"
ls = [BALL, EMPTY, EMPTY]
s = input()
for _, t in enumerate(s):
    if t == "A":
        move_atype(ls)
    elif t == "B":
        move_btype(ls)
    else:
        move_ctype(ls)
print(ls.index(BALL) + 1)
