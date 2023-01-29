row, col = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]
result = [0, 0]
for r in range(row):
    for c in range(col):
        if r < row - 1:
            if board[r][c] and board[r + 1][c]:
                result[0] += 1
                result[1] += 1
        if c < col - 1:
            if board[r][c] and board[r][c + 1]:
                result[0] += 1
                result[1] += 1
        if r < row - 1 and c < col - 1:
            if board[r][c] and board[r + 1][c + 1]:
                result[1] += 1
        if r < row - 1 and c > 0:
            if board[r][c] and board[r + 1][c - 1]:
                result[1] += 1
print(*result)
