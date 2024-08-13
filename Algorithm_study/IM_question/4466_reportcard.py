T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # N개의 과목을 시험 쳤고, K개의 과목을 선택 가능
    scores = list(map(int, input().split()))  # N개 과목의 시험 점수들
    ans = []
    temp = 0
    cnt = 0
    while cnt > K:
        for i in range(N):
            scores[i] > temp
            temp = scores[i]
            if i == N-1:
                ans.append(temp)
                temp = 0