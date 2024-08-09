import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        temp = 0
        t = 0
        for j in range(i+1, N):
            if a[i] <= a[j]:
                temp += 1
        t = N - (i + temp + 1)
        if t > count:
            count = t
    print(f'#{tc} {count}')
