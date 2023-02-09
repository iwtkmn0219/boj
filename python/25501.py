def recursion(s, l, r):
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        global cnt
        cnt += 1
        return recursion(s, l + 1, r - 1)


def isPalindrome(s):
    global cnt
    cnt += 1
    return recursion(s, 0, len(s) - 1)


n = int(input())
for _ in range(n):
    line = input()
    cnt = 0
    result = isPalindrome(line)
    print(result, cnt)
