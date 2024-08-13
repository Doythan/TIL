T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(N)]
    candidate = 0  # 후보지인지 검사 하기 위한 변수
    candidate_num = 0  # 후보지 개수 저장할 변수
    for i in range(N):
        for j in range(M):
            candidate = ground[i][j]
            for ii in range(4):
                for jj in range(4):
                    ni = i + di[ii]
                    nj = j + dj[jj]