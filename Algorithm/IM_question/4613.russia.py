import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    count = 0
    count2 = 0
    ans = float('inf')
    # 완전 탐색으로 문제 해결 w가 제일 많을 경우부터 파악하고 점점 w개수를 줄여가며 최솟값을 찾았음
    for w in range(N-3, -1, -1):
        for b in range(N-2, w, -1):
            r = N - 1
            for i in range(r, b, -1):
                for j in range(M):
                    if flag[i][j] != 'R':
                        count2 += 1
            for i in range(b, w, -1):
                for j in range(M):
                    if flag[i][j] != 'B':
                        count2 += 1
            for i in range(w, -1, -1):
                for j in range(M):
                    if flag[i][j] != 'W':
                        count2 += 1
            if ans > count2:
                ans = count2
            count2 = 0

    print(f'#{tc}', ans)










