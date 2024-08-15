import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    crop = [list(map(int, input())) for _ in range(N)]  # 농작물 2차원 리스트에 공백 없이 입력
    crop_profit = 0  # 농작물 수입
    for i in range(N):
        #  규칙에 맞는 농작물 수익을 더하기 위한 범위 구하기
        if i <= N // 2:
            r1 = N // 2 - i
            r2 = N // 2 + i + 1
        else:
            r1 = abs(N // 2 - i)
            r2 = N - r1

        for j in range(r1, r2):
            crop_profit += crop[i][j]
    print(f'#{tc}', crop_profit)



