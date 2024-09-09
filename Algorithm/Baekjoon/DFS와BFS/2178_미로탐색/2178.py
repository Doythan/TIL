from collections import deque
import sys
sys.stdin = open("input.txt", "r")
# sys.setrecursionlimit(10000)


def bfs(si, sj, ei, ej):
    q = deque([])
    v = [[0] * M for _ in range(N)]
    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우

    q.append([si, sj])
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        # 정답 처리가 필요한 경우 이 자리에서 진행
        if ci == ei and cj == ej:
            return v[ei][ej]

        for k in range(4):
            ni = di[k] + ci
            nj = dj[k] + cj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and v[ni][nj] == 0:
                q.append([ni, nj])
                v[ni][nj] = v[ci][cj] + 1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

ans = bfs(0, 0, N-1, M-1)

print(ans)
