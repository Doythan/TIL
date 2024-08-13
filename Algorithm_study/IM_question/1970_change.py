import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    ans = [0] * 8
    for i in range(8):
        if N // change[i] > 0:
            ans[i] += N // change[i]
            N -= change[i] * (N // change[i])
    print(f'#{tc}')
    print(' '.join(map(str, ans)))
