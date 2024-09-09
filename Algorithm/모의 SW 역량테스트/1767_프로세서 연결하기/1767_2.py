def dfs(d, cores, total_length):  # 깊이, 연결된 코어 수, 총 전선의 길이
    global max_core, min_length

    if d == len(core_position):
        if max_core < cores:
            max_core = cores
            min_length = total_length

        elif max_core == cores:
            min_length = min(min_length, total_length)

        return

    x, y = core_position[d]
    for k in range(4):
        ni, nj = x, y
        length = 0
        while True:
            ni += di[k]
            nj += dj[k]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:  # 전원 연결됨이 끝까지 도달된 경우
                break
            if arr[ni][nj] != 0:
                length = 0
                break
            length += 1
        if length == 0:
            continue

        ni, nj = x, y
        for _ in range(length):
            ni += di[k]
            nj += dj[k]
            arr[ni][nj] = 2

        dfs(d + 1, cores + 1, total_length + length)

        ni, nj = x, y
        for _ in range(length):
            ni += di[k]
            nj += dj[k]
            arr[ni][nj] = 0

    dfs(d + 1, cores, total_length)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 코어 저장
    core_position = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if arr[i][j] == 1:
                core_position.append([i, j])

    max_core = 0
    min_length = float('inf')

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    dfs(0, 0, 0)
    print(min_length)

