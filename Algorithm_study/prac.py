n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
temp = []
ans = []
for i in range(n):
    for j in range(n):
        temp += [str((a[i][j]))]
        print(temp)

    # ans += ["".join(temp)]
    # print(ans)
    # temp = []
    #
