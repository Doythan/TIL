T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        if i != (n-i-1):
            ans += a[i][i] + a[i][n-i-1]
        else:
            ans += a[i][i]
    print(f'#{tc} {ans}')