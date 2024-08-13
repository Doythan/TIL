import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 당근의 개수
    carrots = list(map(int, input().split()))  # 당근의 크기를 의미하는 당근 N개
    cnt = 1  # 연속으로 커지는 당근 개수의 최대값 비교하기 위한 카운트 변수
    ans = 1  # 연속으로 커지는 당근 개수의 최대값
    for i in range(N-1):
        if carrots[i] < carrots[i+1]:
            cnt += 1
            if ans < cnt:
                ans = cnt
        else:
            cnt = 1

    print(f'#{tc}', ans)



