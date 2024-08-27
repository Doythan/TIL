import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N : 배열의 크기, M : 스프레이의 세기
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [-1, 1, 0, 0, -1, -1, 1, 1]
    dj = [0, 0, -1, 1, -1, 1, -1, 1]
    ans, temp = 0, 0
    for i in range(N):
        for j in range(N):
            temp = arr[i][j]
            for k in range(4):
                for l in range(1, M):
                    ni = i + di[k] * l
                    nj = j + dj[k] * l
                    if 0 <= ni < N and 0 <= nj < N:
                        temp += arr[ni][nj]
            if temp > ans:
                ans = temp

            temp = arr[i][j]
            for k in range(4, 8):
                for l in range(1, M):
                    ni = i + di[k] * l
                    nj = j + dj[k] * l
                    if 0 <= ni < N and 0 <= nj < N:
                        temp += arr[ni][nj]
            if temp > ans:
                ans = temp

    print(f'#{tc}', ans)



