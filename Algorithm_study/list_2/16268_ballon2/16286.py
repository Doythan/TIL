T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    new_list = []
    for x in range(N):
        for y in range(M):

            sum_v = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < M:
                    sum_v += arr[nx][ny]

            sum_v += arr[x][y]
            new_list.append(sum_v)

    print(f'#{case}', max(new_list))

