T = int(input)
for tc in range(1, T+1):
    n, m = map(int, (input().split()))
    arr = [list(map(int, input().split())) for _ in range(3)]
    a = 0
    temp = 0
    for i in range(n):
        for j in range(m):
            a = arr[i][j]
            for k in range(a):
                if i-k != 0:
                    temp = temp + a[i-k][j] + a[i][j-k]


