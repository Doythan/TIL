import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    ans_a = ' '.join(map(str, a))
    print(f'#{tc}', ans_a)
