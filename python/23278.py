n, l, h = map(int, input().split())
evaluation = sorted(list(map(int, input().split())))
print(f"{sum(evaluation[l:n - h])/(n - l - h):.10f}")
