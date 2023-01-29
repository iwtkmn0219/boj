k = int(input())
for dataset in range(k):
    n, v = map(int, input().split())
    dic = {i + 1: list(map(int, input().split())) for i in range(n)}
    pay = 0
    for _ in range(v):
        ad1, ad2, user_type = map(int, input().split())
        if dic[ad1][0]:
            pay += dic[ad1][1]
        if dic[ad2][0]:
            pay += dic[ad2][1]
        if user_type == 1 and not dic[ad1][0]:
            pay += dic[ad1][1]
        elif user_type == 2 and not dic[ad2][0]:
            pay += dic[ad2][1]
    print(f"Data Set {dataset + 1}:\n{pay}\n")
