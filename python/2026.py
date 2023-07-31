def show_vector(v):
    for i in range(1, len(v)):
        print(v[i])

def correct(v, relation):
    for i in range(1, len(v) - 2):
        for j in range(i + 2, len(v)):
            if not relation[v[i]][v[j]]:
                return False
    return True

def permutation(picked, relation, k):
    if len(picked) == k + 1:
        if correct(picked, relation):
            show_vector(picked)
            return True
        return False

    current = picked[-1]
    for next_node in range(len(relation)):
        if relation[current][next_node]:
            picked.append(next_node)
            condition = permutation(picked, relation, k)
            if condition:
                return True
            picked.pop()

    return False

def main():
    k, n, f = map(int, input().split())
    relation = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(f):
        x, y = map(int, input().split())
        if y < x:
            x, y = y, x
        relation[x][y] = True

    if k == 1:
        print(1)
        return

    for i in range(1, n + 1):
        relation[0][i] = True

    v = [0]
    if not permutation(v, relation, k):
        print(-1)

if __name__ == "__main__":
    main()
