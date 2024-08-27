import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    omok = [list(input()) for _ in range(N)]
    di = [-1, 1, 0, 0, -1, 1, -1, 1]  # 세로, 가로, 왼쪽 대각선, 오른쪽 대각선 행 좌표
    dj = [0, 0, -1, 1, -1, 1, 1, -1]  # 세로, 가로, 왼쪽 대각선, 오른쪽 대각선 행 좌표
    check = 0  # 프로그램을 종료시킬 조건 체크 변수
    ans = 'NO'
    for i in range(N):
        for j in range(N):
            temp = omok[i][j]
            if temp == 'o':
                # 상,하를 기준으로 오목인지 체크
                cnt = 0
                for k in range(2):
                    for l in range(1, 3):
                        ni = i + di[k] * l
                        nj = j + dj[k] * l
                        if 0 <= ni < N and 0 <= nj < N:
                            if omok[ni][nj] == 'o':
                                cnt += 1
                if cnt == 4:
                    ans = 'YES'
                    check = 1
                    break
                cnt = 0
                # 좌, 우를 기준으로 오목인지 체크
                cnt = 0
                for k in range(2, 4):
                    for l in range(1, 3):
                        ni = i + di[k] * l
                        nj = j + dj[k] * l
                        if 0 <= ni < N and 0 <= nj < N:
                            if omok[ni][nj] == 'o':
                                cnt += 1
                if cnt == 4:
                    ans = 'YES'
                    check = 1
                    break
                cnt = 0
                # 왼쪽 대각선을 기준으로 오목인지 체크
                cnt = 0
                for k in range(4, 6):
                    for l in range(1, 3):
                        ni = i + di[k] * l
                        nj = j + dj[k] * l
                        if 0 <= ni < N and 0 <= nj < N:
                            if omok[ni][nj] == 'o':
                                cnt += 1
                if cnt == 4:
                    ans = 'YES'
                    check = 1
                    break
                cnt = 0
                # 오른쪽 대각선을 기준으로 오목인지 체크
                cnt = 0
                for k in range(6, 8):
                    for l in range(1, 3):
                        ni = i + di[k] * l
                        nj = j + dj[k] * l
                        if 0 <= ni < N and 0 <= nj < N:
                            if omok[ni][nj] == 'o':
                                cnt += 1
                if cnt == 4:
                    ans = 'YES'
                    check = 1
                    break
            if check == 1: break
        if check == 1: break
    print(f'#{tc}', ans)


# 우영이형 코드
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(input()) for _ in range(N)]
#     ans = 'NO'
#     flag = 0
#
#     # 행 기준 확인
#     for i in range(N):
#         cnt = 0
#         if flag == 1:
#             break  # for i 문
#         for j in range(N):
#             if arr[i][j] == 'o':
#                 cnt += 1
#             else:
#                 if cnt == 5:
#                     ans = 'YES'
#                     flag = 1
#                     break # for j 문
#                 cnt = 0
#         if cnt == 5:
#             ans = 'YES'
#             flag = 1
#
#     # 열 기준 확인
#     if flag == 0:
#         for i in range(N):
#             cnt = 0
#             if flag == 1:
#                 break  # for i 문
#             for j in range(N):
#                 if arr[j][i] == 'o':
#                     cnt += 1
#                 else:
#                     if cnt == 5:
#                         ans = 'YES'
#                         flag = 1
#                         break # for j 문
#                     cnt = 0
#             if cnt == 5:
#                 ans = 'YES'
#                 flag = 1
#
#     # 대각선1 확인
#     if flag == 0:
#         for i in range(N * 2 - 1):
#             if flag == 1:
#                 break # for i 문
#             for x in range(N):
#                 if flag == 1:
#                     break
#                 for y in range(N):
#                     if x + y == i:
#                         if arr[x][y] == 'o':
#                             cnt += 1
#                         else:
#                             if cnt == 5:
#                                 ans = 'YES'
#                                 flag = 1
#                                 break # for y 문
#                             cnt = 0
#             if cnt == 5:
#                 ans = 'YES'
#                 flag = 1
#
#     # 90도 회전 시키기
#     # 1. 전치 시키기
#     if flag == 0:
#         for i in range(N):
#             for j in range(N):
#                 if i > j:
#                     arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
#
#     # 2. 역 슬라이싱
#     if flag == 0:
#         for k in range(N):
#             arr[k] = arr[k][::-1]
#
#
#     # 대각선2 확인
#     if flag == 0:
#         for i in range(N * 2 - 1):
#             if flag == 1:
#                 break # for i 문
#             for x in range(N):
#                 if flag == 1:
#                     break
#                 for y in range(N):
#                     if x + y == i:
#                         if arr[x][y] == 'o':
#                             cnt += 1
#                         else:
#                             if cnt == 5:
#                                 ans = 'YES'
#                                 flag = 1
#                                 break # for y 문
#                             cnt = 0
#             if cnt == 5:
#                 ans = 'YES'
#                 flag = 1
#
#     print(f'#{tc} {ans}')


