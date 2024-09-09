from collections import deque


def bfs(si, sj):
    q = deque([])
    v = [[0] * 16 for _ in range(16)]
    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

    q.append([si, sj])
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        if arr[ci][cj] == 3:  # 도착점 도달 시
            return 1

        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]

            # 범위 내에 있고, 방문하지 않았으며, 벽이 아니면 이동
            if 0 <= ni < 16 and 0 <= nj < 16 and (arr[ni][nj] == 0 or arr[ni][nj] == 3) and v[ni][nj] == 0:
                q.append([ni, nj])
                v[ni][nj] = 1

    return 0  # 도착점에 도달하지 못했을 때


for tc in range(1, int(input()) + 1):  # 테스트 케이스 반복
    arr = [list(map(int, input().strip())) for _ in range(16)]
    print(f'#{tc} {bfs(1, 1)}')
