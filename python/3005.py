r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
result = "{"  # Unicode: 123 (z: 122)
for i in range(r):
    for j in range(c):
        if i == 0 or board[i - 1][j] == "#":
            row_idx = i
            row_result = ""
            while row_idx < r:
                if board[row_idx][j] == "#":
                    break
                row_result += board[row_idx][j]
                row_idx += 1
            if len(row_result) > 1:
                result = min(result, row_result)
        if j == 0 or board[i][j - 1] == "#":
            col_idx = j
            col_result = ""
            while col_idx < c:
                if board[i][col_idx] == "#":
                    break
                col_result += board[i][col_idx]
                col_idx += 1
            if len(col_result) > 1:
                result = min(result, col_result)
print(result)
