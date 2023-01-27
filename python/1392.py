n, q = map(int, input().split())
music_sheet = []
for i in range(n):
    time = int(input())
    for _ in range(time):
        music_sheet.append(i + 1)
for i in range(q):
    print(music_sheet[int(input())])
