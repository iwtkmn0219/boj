DNA_DIC = {
    "AA": "A",
    "AG": "C",
    "AC": "A",
    "AT": "G",
    "GA": "C",
    "GG": "G",
    "GC": "T",
    "GT": "A",
    "CA": "A",
    "CG": "T",
    "CC": "C",
    "CT": "G",
    "TA": "G",
    "TG": "A",
    "TC": "G",
    "TT": "T",
}


n = int(input())
s = input()

for _ in range(n - 1):
    s = s[:-2] + DNA_DIC[s[-2:]]
print(s)
