import sys
sys.stdin = open("input.txt", "r")

T = int(input())

#  우, 하, 좌, 상, 좌상, 우상, 좌하, 우하
di = [0, 1, 0, -1, -1, -1, 1, 1]
dj = [1, 0, -1, 0, -1, 1, -1, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(N)]

    candidate = 0  # 후보지 주변 낮은 구역을 카운트 할 변수
    candidate_num = 0  # 후보지 개수를 카운트 할 변수
    for i in range(N):
        for j in range(M):
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if ground[ni][nj] < ground[i][j]:
                        candidate += 1
            if candidate >= 4:
                candidate_num += 1
            candidate = 0
    print(f'#{tc}', candidate_num)



