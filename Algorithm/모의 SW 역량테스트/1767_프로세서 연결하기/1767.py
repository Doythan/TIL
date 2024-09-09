import sys
sys.stdin = open("input.txt", "r")


def dfs(d, cores, total_length):  # 깊이, 코어의 수, 전체 전선의 길이
    global max_cores, min_length

    # 종료조건
    if d == len(core_position):
        if cores > max_cores:
            max_cores = cores
            min_length = total_length

        elif cores == max_cores:
            min_length = min(min_length, total_length)
        return

    x, y = core_position[d]  # 현재 코어의 위치
    for k in range(4):
        ni, nj = x, y
        length = 0
        # 전선 설치 가능 여부
        while True:
            ni += dx[k]
            nj += dy[k]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:  # 전원이 연결됨 끝까지 도달
                break
            if arr[ni][nj] != 0:  # 다른 전선이나 코어에 부딪힌 경우
                length = 0
                break
            length += 1
        if length == 0:  # 연결이 불가능 하다면 다음 방향
            continue

        ni, nj = x, y
        for _ in range(length):
            ni += dx[k]
            nj += dy[k]
            arr[ni][nj] = 2  # 전선은 2로 표현

        dfs(d + 1, cores + 1, total_length + length)

        # 백트래킹 (전선 제거)
        ni, nj = x, y
        for _ in range(length):
            ni += dx[k]
            nj += dy[k]
            arr[ni][nj] = 0  # 전선 제거

    # 현재 코어를 연결하지 않고 넘어가는 경우도 고려
    dfs(d + 1, cores, total_length)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 코어 위치 저장
    core_position = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if arr[i][j] == 1:
                core_position.append([i, j])

    max_cores = 0  # 최대 연결된 코어 수
    min_length = float('inf')  # 최소 전선 길이의 합

    # 델타(상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dfs(0, 0, 0)

    print(f'#{tc}', min_length)

