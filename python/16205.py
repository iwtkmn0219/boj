def camel(s: str) -> str:
    if "_" in s:
        result = ""
        for i in range(len(s)):
            if i == 0:
                result = s[i].lower()
                continue
            if s[i - 1] == "_":
                result += s[i].upper()
            else:
                if s[i] == "_":
                    continue
                result += s[i]
        return result
    result = ""
    if ord(s[0]) < 97:
        for i in range(len(s)):
            if i == 0:
                result += s[i].lower()
                continue
            result += s[i]
        return result
    else:
        return s


def snake(s: str) -> str:
    if "_" in s:
        return s
    result = ""
    for i in range(len(s)):
        if i == 0:
            result += s[i].lower()
            continue
        if ord(s[i]) < 97:
            result += "_" + s[i].lower()
        else:
            result += s[i]
    return result


def pascal(s: str) -> str:
    if "_" in s:
        result = ""
        for i in range(len(s)):
            if i == 0:
                result = s[i].upper()
                continue
            if s[i - 1] == "_":
                result += s[i].upper()
            else:
                if s[i] == "_":
                    continue
                result += s[i]
        return result
    result = ""
    if ord(s[0]) >= 97:
        for i in range(len(s)):
            if i == 0:
                result += s[i].upper()
                continue
            result += s[i]
        return result
    else:
        return s


s = list(input().split())
print(camel(s[1]))
print(snake(s[1]))
print(pascal(s[1]))
