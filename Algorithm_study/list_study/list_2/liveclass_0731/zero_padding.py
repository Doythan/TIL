n = int(input())

a = [[0] * (n+2)]
a = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
a += [[0] * (n+2)]
print(a)