import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # N개의 과목을 시험 쳤고, K개의 과목을 선택 가능
    scores = list(map(int, input().split()))  # N개 과목의 시험 점수들
    ans = []
    cnt, temp_max = 0, 0
    sum_score = 0
    while True:
        for i in range(N):
            if scores[i] > temp_max:
                temp_max = scores[i]
        cnt += 1
        for i in range(N):
            if scores[i] == temp_max:
                scores[i] = 0
                break
        ans.append(temp_max)
        temp_max = 0
        if cnt == K:
            break
    for i in range(K):
        sum_score += ans[i]
    print(f'#{tc}', sum_score)




