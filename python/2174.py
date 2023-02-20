nwse = [[1, 0], [0, -1], [-1, 0], [0, 1]]

a, b = map(int, input().split())
board = [[0] * (a + 1) for _ in range(b + 1)]
n, m = map(int, input().split())
robots = [[0] * 3 for _ in range(n + 1)]
for i in range(1, n + 1):
    line = input().split()
    x = int(line[0])
    y = int(line[1])
    direction = line[2]
    robots[i][0] = x
    robots[i][1] = y
    if direction == "N":
        robots[i][2] = 0
    elif direction == "W":
        robots[i][2] = 1
    elif direction == "S":
        robots[i][2] = 2
    else:
        robots[i][2] = 3
    board[y][x] = i

ERROR = False
for _ in range(m):
    line = input().split()
    robot_number = int(line[0])
    order = line[1]
    loop = int(line[2])
    if order == "F":
        forward = robots[robot_number][2]
        for _ in range(loop):
            prev_x = robots[robot_number][0]
            prev_y = robots[robot_number][1]
            robots[robot_number][0] += nwse[forward][1]
            robots[robot_number][1] += nwse[forward][0]
            xx = robots[robot_number][0]
            yy = robots[robot_number][1]
            if 0 < xx <= a and 0 < yy <= b:
                if board[yy][xx] == 0:
                    board[yy][xx] = robot_number
                    board[prev_y][prev_x] = 0
                else:
                    print(f"Robot {robot_number} crashes into robot {board[yy][xx]}")
                    ERROR = True
                    break
            else:
                print(f"Robot {robot_number} crashes into the wall")
                ERROR = True
                break
    elif order == "L":
        robots[robot_number][2] = (robots[robot_number][2] + loop) % 4
    elif order == "R":
        robots[robot_number][2] = (robots[robot_number][2] - loop) % 4
    if ERROR:
        break
if not ERROR:
    print("OK")
