board = [list(input()) for _ in range(8)]

cnt = 0
for i in range(8):
    for j in range(8):
        if board[i][j] == "R":
            for col in range(j):
                if board[i][col] == "R":
                    break
                board[i][col] = "X"
            for col in range(j + 1, 8):
                if board[i][col] == "R":
                    break
                board[i][col] = "X"
            for row in range(i):
                if board[row][j] == "R":
                    break
                board[row][j] = "X"
            for row in range(i + 1, 8):
                if board[row][j] == "R":
                    break
                board[row][j] = "X"
for i in range(8):
    for j in range(8):
        if board[i][j] == ".":
            cnt += 1
print(cnt)
