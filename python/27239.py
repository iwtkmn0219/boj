n = int(input())
print(f"{chr((n - 1) % 8 + 97)}{n // 9 + 1}")
