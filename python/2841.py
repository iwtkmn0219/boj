import sys

input = sys.stdin.readline


def binary_search(ls: list, value: int) -> int:
    start = 0
    end = len(ls) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if ls[mid] >= value:
            end = mid
        else:
            start = mid
    if value <= ls[start]:
        return start
    elif value <= ls[end]:
        return end


guitar = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
n, p = map(int, input().split())
cnt = 0
for melody in range(n):
    string, fret = map(int, input().split())

    # 해당 string에서 아무것도 눌려있지 않은 경우
    if len(guitar[string]) == 0:
        guitar[string].append(fret)
        cnt += 1
    else:
        if guitar[string][-1] == fret:
            continue

        if guitar[string][-1] < fret:
            guitar[string].append(fret)
            cnt += 1
        else:
            idx = binary_search(guitar[string], fret)
            if guitar[string][idx] == fret:
                cnt += len(guitar[string]) - (idx + 1)
                guitar[string] = guitar[string][: (idx + 1)]
            else:
                cnt += len(guitar[string]) - idx + 1
                guitar[string] = guitar[string][:idx] + [fret]
print(cnt)
