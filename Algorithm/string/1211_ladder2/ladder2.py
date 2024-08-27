import sys
sys.stdin = open("input.txt", "r")


for _ in range(10):
    tc = int(input())
    N = 100  # 사다리 크기
    a = [[0] * (100+2)]
    a += [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    a += [[0] * (100+2)]
    min_v = 0
    for j in range(1, N+1):
        cnt = 0
        jj = j
        if a[1][j] == 1:
            cnt += 1
            for i in range(2, N+1):
                cnt += 1
                check_1, check_2 = 0, 0
                while True:
                    if a[i][jj-1] == 1 and check_1 == 0:
                        cnt += 1
                        check_2 += 1
                        jj = jj-1
                    elif a[i][jj+1] == 1 and check_2 == 0:
                        cnt += 1
                        check_1 += 1
                        jj = jj+1
                    else:
                        break
        if j == 1:
            min_v = cnt
            ans = j
            cnt = 0
        elif min_v > cnt and a[1][j] == 1:
            min_v = cnt
            ans = j
    print(f'#{tc}', ans-1)





