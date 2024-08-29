import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]  # 8 * 56 암호코드를 포함하는 N * M 직사각형 2차원 리스트 입력
    temp = -1  # 맨 처음 1을 탐색했을때 열의 인덱스
    x = 0
    cnt = 0
    idx = 0
    ans = [[] for _ in range(8)]
    codes = [
        ['0001101'], ['0011001'], ['0010011'], ['0111101'], ['0100011'],
        ['0110001'], ['0101111'], ['0111011'], ['0110111'], ['0001011']
    ]
    # 배열안에서 처음 1을 찾는 루프
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if arr[i][j] == '1':
                temp = j
                break
        if temp != -1:
            break
    x = i
    for j in range(temp - 55, temp + 1):
        ans[idx].append(arr[x][j])
        cnt += 1
        if cnt == 7:
            cnt = 0
            idx += 1
    result = [''.join(ans[idx]) for idx in range(8)]
    odd, even = 0, 0

    for i in range(8):
        for j in range(10):
            if result[i] == codes[j][0]:
                if i % 2 == 0:
                    odd += j
                elif i % 2 == 1:
                    even += j

    if ((odd * 3) + even) % 10 == 0:
        print(f'#{tc}', odd + even)
    else:
        print(f'#{tc}', 0)



