import sys

input = sys.stdin.readline

database = {}
n = int(input())
cnt = 0
for _ in range(n):
    line = input()[:-1]
    if line == "ENTER":
        database.clear()
        continue
    if line not in database:
        database[line] = 1
        cnt += 1
print(cnt)
