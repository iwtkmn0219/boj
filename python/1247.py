import sys

input = sys.stdin.readline

for tc in range(3):
    n = int(input())
    sum_of_numbers = 0
    for _ in range(n):
        sum_of_numbers += int(input())
    if sum_of_numbers == 0:
        print(0)
    elif sum_of_numbers < 0:
        print("-")
    else:
        print("+")
