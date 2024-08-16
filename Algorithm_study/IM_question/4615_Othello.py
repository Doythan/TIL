import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N : 보드의 크기, M : 플레이어가 놓는 돌 개수
    board = [[0] * N for _ in range(N)]  # N * N 보드 만들기
    #  보드의 초기 흰돌, 검은돌 설정 검은 돌 : 1, 흰 돌: 2
    board[N // 2][N // 2], board[N // 2 - 1][N // 2 - 1] = 2, 2
    board[N // 2][N // 2 - 1], board[N // 2 - 1][N // 2] = 1, 1

    for _ in range(M):
        j, i, dol = map(int, input().split())  # 놓을 돌 위치와 종류 입력
        di = [-1, 1, 0, 0, -1, 1, -1, 1]  # 행 기준 : 상, 하, 좌, 우, 상좌, 하우, 상우, 하좌
        dj = [0, 0, -1, 1, -1, 1, 1, -1]  # 열 기준 : 상, 하, 좌, 우, 상좌, 하우, 상우, 하좌
        board[i-1][j-1] = dol  # 입력 받은 위치에 입력받은 돌 놓기

        for k in range(8):  # 8방향 검사를 위한 반복문
            for l in range(2, N):
                ni = (i - 1) + di[k] * l
                nj = (j - 1) + dj[k] * l
                if 0 <= ni < N and 0 <= nj < N:
                    if board[(i-1)+di[k]][(j-1)+dj[k]] != dol and board[(i-1)+di[k]][(j-1)+dj[k]] != 0:
                        if board[ni][nj] == 0:
                            break
                        elif board[ni][nj] == dol:
                            for p in range(1, l):
                                ni = (i - 1) + di[k] * p
                                nj = (j - 1) + dj[k] * p
                                board[ni][nj] = dol
                    else:
                        break

    B = 0
    W = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                B += 1
            elif board[i][j] == 2:
                W += 1

    print(f'#{tc}', B, W)






